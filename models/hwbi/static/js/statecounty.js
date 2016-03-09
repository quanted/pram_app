$(document).ready(function(){
    var stateObject = {};
    $.getJSON('/static/json/statecounty.json', function(data) {
        $.each(data, function(index, val) {
            stateObject[index] = val;
        });

        var stateSel = document.getElementById("stateSel");
        var countySel = document.getElementById("countySel");

        for (var state in stateObject) {
            stateSel.options[stateSel.options.length] = new Option(state, state);
        }

         stateSel.onchange = function () {
             countySel.length = 1; // remove all options bar first
             if (this.selectedIndex < 1) return; // done
             for (var county in stateObject[this.value]) {
                 countySel.options[countySel.options.length] = new Option(stateObject[this.value][county], stateObject[this.value][county]);
            }
        }
    });
    

    //on county selection, send ajax get call sending state and county name to server
    $('#countySel').change(function () {
        //old visual studio call-> http://localhost:64399/api/Baseline?State=Georgia&County=Appling
        //NEW call-> http://134.67.114.8/hwbi/api/Baseline?State=Georgia&County=Appling
        var state = $('#stateSel').val();
        var county = $('#countySel').val();
        $.getJSON('/ubertool/hwbi/api/Baseline?State=' + state + '&County=' + county, function(data) {
            updateRIVWeights(data.Domains);
            updateDomainScores(data.Domains);
            updateDomainScores2(data.Domains);
            updateServiceScores(data.Services);
        });
    });
    

    //function to update RIV domain weight values
    function updateRIVWeights(domains) {
        //console.log(domains);
        $('#ConnectionToNatureDomainWeight').val(domains[0].Weight);
        $('#CulturalFulfillmentDomainWeight').val(domains[1].Weight);
        $('#EducationDomainWeight').val(domains[2].Weight);
        $('#HealthDomainWeight').val(domains[3].Weight);
        $('#LeisureTimeDomainWeight').val(domains[4].Weight);
        $('#LivingStandardsDomainWeight').val(domains[5].Weight);
        $('#SafetyAndSecurityDomainWeight').val(domains[6].Weight);
        $('#SocialCohesionDomainWeight').val(domains[7].Weight);
    }
});