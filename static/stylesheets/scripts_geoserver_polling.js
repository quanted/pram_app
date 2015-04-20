// Long polling for SAM results
$( document ).ready(function() {

    $('.sam_map').show();

    // Warn user not to refresh page
    alert('SAM run successfully submitted.  Do NOT refresh page.  ' +
        'This will result in duplicate model submissions and will slow down returning of model results.');

    var jid_ajax = document.getElementById('jid').innerHTML; // SAM run 'jid'
    //var timer = null;

    function updateTimer() {

        $.ajax({ 
            url: "/geoserver/sam_done/" + jid_ajax,
            method: 'POST',
            // dataType: "text",
            success: function(data) {
                
                //console.log(data);

                if (data == "done") {
                    //clearTimeout(timer);
                    showMap();
                    $('.sam_link').show();
                } else {
                    setTimeout(updateTimer, 10000); // poll every 10s until success
                }
1
            },
            error: function( jqXHR, textStatus, errorThrown ){
                console.log(jqXHR);
                console.log(textStatus);
                console.log(errorThrown);

                setTimeout(updateTimer, 10000); // poll every 10s until success
            }

        });

    }

    function showMap() {

        sam_output_layer = new OpenLayers.Layer.WMS(
            "SAM SQL View",
            "http://134.67.114.4/geoserver/cite/wms",
            {
                "LAYERS": 'cite:joinTest',
                "STYLES": 'joinTestStyle',
                "format": format,
                "viewparams": 'jid:test1',
                "env": 'r1:2;r2:4;r3:6;r4:8;r5:10'
            },
            {
                buffer: 0,
                displayOutsideMaxExtent: true,
                isBaseLayer: true,
                yx : {'EPSG:3857' : false}
            }
        );

        map.removeLayer(tiled);
        map.addLayers([sam_output_layer]);
        console.log("Tried to switch baselayer");

        // support GetFeatureInfo
        map.events.register('click', map, function (e) {

            document.getElementById('nodelist').innerHTML = "Loading... please wait...";
            var params = {
                REQUEST: "GetFeatureInfo",
                EXCEPTIONS: "application/vnd.ogc.se_xml",
                BBOX: map.getExtent().toBBOX(),
                SERVICE: "WMS",
                INFO_FORMAT: 'application/json',  // If set to 'text/html', returned HTML is formatted using templates on Geoserver
                QUERY_LAYERS: map.layers[0].params.LAYERS,
                FEATURE_COUNT: 50,
                "Layers": 'cite:joinTest',
                WIDTH: map.size.w,
                HEIGHT: map.size.h,
                format: format,
                //styles: map.layers[0].params.STYLES,
                srs: map.layers[0].params.SRS};

            // handle the wms 1.3 vs wms 1.1 madness
            if(map.layers[0].params.VERSION == "1.3.0") {
                params.version = "1.3.0";
                params.j = parseInt(e.xy.x);
                params.i = parseInt(e.xy.y);
            } else {
                params.version = "1.1.1";
                params.x = parseInt(e.xy.x);
                params.y = parseInt(e.xy.y);
            }

            // merge filters
            if(map.layers[0].params.CQL_FILTER != null) {
                params.cql_filter = map.layers[0].params.CQL_FILTER;
            }
            if(map.layers[0].params.FILTER != null) {
                params.filter = map.layers[0].params.FILTER;
            }
            if(map.layers[0].params.FEATUREID) {
                params.featureid = map.layers[0].params.FEATUREID;
            }
            //                                                                 caller onComplete onFailure
            OpenLayers.loadURL("http://134.67.114.4/geoserver/cite/wms", params, this, setHTML, setHTML);
            OpenLayers.Event.stop(e);
        });
    }

    updateTimer(); //initiate the timer
});
