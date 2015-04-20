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
            "cite:huc12s05 - Tiled",
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
    }

    updateTimer(); //initiate the timer
});
