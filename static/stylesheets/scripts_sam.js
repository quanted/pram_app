$(document).ready(function() {
	// Call function to setup tabbed nav
    uberNavTabs(
        ["Chemical", "Application", "Simulation", "Output"],
        {   "isSubTabs":false   }
    );

	// Set default start date
	startDate = $("#id_sim_date_start").val();
	$( "#id_sim_date_start" ).datepicker({
		changeYear: true,
		yearRange: '1960:+nn',
		defaultDate: startDate
	});
	// Set default end date
	endDate = $("#id_sim_date_end").val();
	$( "#id_sim_date_end" ).datepicker({
		changeYear: true,
		yearRange: '1960:+nn',
		defaultDate: endDate
	});
	// Set default first app date
	firstAppDate = $("#id_sim_date_1stapp").val();
	$( "#id_sim_date_1stapp" ).datepicker({
		changeYear: true,
		yearRange: '1960:+nn',
		defaultDate: firstAppDate
	});

});