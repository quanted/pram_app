$(document).ready(function() {
	// Call function to setup tabbed nav
    uberNavTabs(
        ["Chemical", "Application", "Simulation", "Output"],
        {   "isSubTabs":false   }
    );

    // Default inputs
    $('#id_sim_type_0, #id_output_format_0').prop('checked', true);
    $('#id_region').val('Ohio Valley');
    $('#id_crop_number').css('color', 'grey');
    $('#id_output_tox_value, #id_output_tox').closest('tr').hide();
    $('#id_refine_time_window2, #id_refine_percent_applied2').prop('disabled', true).closest('tr').hide();;

	// Set default start date
	startDate = $("#id_sim_date_start").val();
	$( "#id_sim_date_start" ).datepicker({
		changeYear: true,
		minDate: new Date(1984, 0, 1),
		maxDate: new Date(2013, 11, 31),
		yearRange: '1984:+2013',
		defaultDate: startDate
	});
	// Set default end date
	endDate = $("#id_sim_date_end").val();
	$( "#id_sim_date_end" ).datepicker({
		changeYear: true,
		minDate: new Date(1984, 0, 1),
		maxDate: new Date(2014, 5, 2),
		yearRange: '1960:+nn',
		defaultDate: endDate
	});
	// Set default first app date
	firstAppDate = $("#id_sim_date_1stapp").val();
	$( "#id_sim_date_1stapp" ).datepicker({
		changeYear: true,
		minDate: new Date(1984, 0, 1),
		maxDate: new Date(2013, 11, 31),
		yearRange: '1960:+nn',
		defaultDate: firstAppDate
	});

	// Selected Crops Rows
	$('#id_crop').closest('tr').after('<tr><th>Chosen Crop(s):</th><td id="crop1"></td></tr>');
	var crop_list_array = [];
	$('#id_crop').change(function() {
		var crop = $("#id_crop option:selected").text();
		if (crop_list_array.length < 4) {
			if ($('#crop1').text() == '') {
				$('#crop1').html(crop + " <span class='deleteCrop'>[x]</span>");
				crop_list_array.push(crop);
			} else {
				if ($.inArray(crop, crop_list_array) == -1) {
					$('#crop1').closest('tr')
					.after('<tr><th></th><td>' + crop + " <span class='deleteCrop'>[x]</span>" + '</td></tr>');
					crop_list_array.push(crop);
				}
			}
		}
		if (crop_list_array.length == 4) {
			$('#id_crop').prop('disabled', true);
		}
		$('#id_crop_number').val(crop_list_array.length);
	});

	$('table').on('click', 'span', function() {
		var removedCropName = $(this).closest('td').text().split(' ')[0];
		var removedCropName_index = $.inArray(removedCropName, crop_list_array);
		if (removedCropName_index < 4) {
			$('#id_crop').prop('disabled', false);
		}
		if ($(this).closest('td').prop('id') == 'crop1') {
			if (crop_list_array.length > 1) {
				$(this).closest('tr').next().find('th').text('Chosen Crop(s):');
				$(this).closest('tr').next().find('td').attr('id', 'crop1');
				$(this).closest('tr').remove();
				crop_list_array.splice(removedCropName_index, 1);
			}
		} else {
			$(this).closest('tr').remove();
			crop_list_array.splice(removedCropName_index, 1);
		}
		$('#id_crop_number').val(crop_list_array.length);
	});

	// Refinements
	$('#id_refine').change(function() {
		var refinement = $(this).val();
		if (refinement == "1") {
			$('#id_refine_time_window2, #id_refine_percent_applied2')
				.prop('disabled', true).closest('tr').hide();
			$('#id_refine_percent_applied1')
				.prop('disabled', false).closest('tr').show();
		}
		else if (refinement == "2") {
			$('#id_refine_percent_applied1, #id_refine_time_window2, #id_refine_percent_applied2')
				.prop('disabled', false).closest('tr').show();
		}
		else if (refinement == "3") {
			$('#id_refine_percent_applied1, #id_refine_time_window2, #id_refine_percent_applied2')
				.prop('disabled', true).closest('tr').hide();
		}
	});

	// Toxicity Threshold
	$('#id_output_type').change(function() {
		var outputType = $(this).val();
		if (outputType == '3') {
			$('#id_output_tox_value, #id_output_tox').closest('tr').show();
		}
		else {
			$('#id_output_tox_value, #id_output_tox').closest('tr').hide();
		}
	});

});