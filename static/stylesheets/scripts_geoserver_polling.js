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
                    //showMap();
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
        $('#sam_still_working').show();
        $('.sam_map').show();
    }

    updateTimer(); //initiate the timer
});
