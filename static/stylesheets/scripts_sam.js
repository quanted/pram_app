$(document).ready(function() {
	// Call function to setup tabbed nav
	uberNavTabs(
		["Chemical", "Application", "Simulation", "Output"],
		{   "isSubTabs":false   }
	);

	// Default inputs
	$('#id_sim_type_0, #id_output_format_0, #id_output_format_1, #id_output_tox_0, #id_output_tox_1').prop('checked', true);
	$('#id_region').val('Ohio Valley');
	$('#id_crop_number').css('color', 'grey');
	$('#id_refine_time_window2, #id_refine_percent_applied2').prop('disabled', true).closest('tr').hide();
	$('#id_crop').closest('tr').after('<tr><th>Chosen Crop(s):</th><td id="crop1"></td></tr>');
	$('#id_output_tox_value').closest('tr').after(
		'<tr><th>Output Summary:</th><td>21-d Average Concentrations - 90<sup>th</sup> percentile</td></tr>' +
		'<tr><th></th><td>60-d Average Concentrations - 90<sup>th</sup> percentile</td></tr>' +
		'<tr><th></th><td>Toxicity Threshold - Average Duration of Daily Exceedances</td></tr>' +
		'<tr><th></th><td>Toxicity Threshold - Percentage of Days with Exceedances</td></tr>'
	);
	var cropsArray_soybeans = ['Soybeans', 'Soybeans/cotton', 'Soybeans/wheat', 'Soybeans/grains'];
	var cropsArray_corn = ['Corn', 'Corn/soybeans', 'Corn/wheat', 'Corn/grains'];
	var crop_list_array = [];
	var samScenarioInputs_atrazine_corn = ["1", "Atrazine", "100", "123", "0", "4", "1500", "1", "1.3", "2", "7", "50", "43", "50", "Ohio Valley", "1", "2", "3", "01/01/1984", "12/31/2013", "04/20/1984", "1", "", "", "4"];
	var samScenarioInputs_chlorpyrifos_corn = ["2", "Chlorpyrifos", "6040", "109", "0", "4", "900", "1", "1.1", "1", "30", "100", "", "", "Ohio Valley", "1", "2", "3", "01/01/1984", "12/31/2013", "04/20/1984", "1", "", "", "4"];
	var samScenarioInputs_chlorpyrifos_soybeans = ["3", "Chlorpyrifos", "6040", "109", "0", "4", "1260", "1", "1.1", "1", "42", "100", "", "", "Ohio Valley", "1", "2", "3", "01/01/1984", "12/31/2013", "04/20/1984", "1", "", "", "4"];
	var samScenarioInputs_fipronil_corn = ["4", "Fipronil", "727", "128", "0", "4", "1500", "1", "0.1", "2", "7", "50", "43", "50", "Ohio Valley", "1", "2", "3", "01/01/1984", "12/31/2013", "04/20/1984", "1", "", "", "4"];
	var samScenarioInputs_metolachlor_corn = ["5", "Metolachlor", "181", "49", "0", "4", "1500", "1", "1.05", "2", "7", "50", "43", "50", "Ohio Valley", "1", "2", "3", "01/01/1984", "12/31/2013", "04/20/1984", "1", "", "", "4"];
	var selectedScenarioValue = $('#id_scenario_selection').val();
	if (selectedScenarioValue !== '0') {
		$(':input:not(#id_scenario_selection, :button)').attr('disabled', true);
		switch (selectedScenarioValue) {
			case '1':
				samFillScenarioCrops('1');
				break;
			case '2':
				samFillScenarioCrops('2');
				break;
			case '3':
				samFillScenarioCrops('3');
				break;
			case '4':
				samFillScenarioCrops('4');
				break;
			case '5':
				samFillScenarioCrops('5');
				break;
			default:
				samFillScenarioCrops('1');
		}
	}
	else {
		$('button.submit').attr('disabled', true);
	}

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

	// Scenario Selector
	function samFillScenarioValues(scenario) {
		$('form :input').not(':button').each(function(i) {
			$(this).val(scenario[i]);
		});
	}	
	function samFillScenarioCrops(scenario) {
		resetCropRows();
		var cropsArray;
		
		switch (scenario) {

			case '1':
				$(':input:not(#id_scenario_selection, :button)').attr('disabled', true);
				$('button.submit').attr('disabled', false);
				$('#id_refine_time_window2, #id_refine_percent_applied2').closest('tr').show();
				samFillScenarioValues(samScenarioInputs_atrazine_corn);
				cropsArray = cropsArray_corn;
				for (i=0;i<cropsArray.length;i++) {
					cropArrayGenerator(cropsArray[i]);
				}
				break;
			case '2':
				$(':input:not(#id_scenario_selection, :button)').attr('disabled', true);
				$('button.submit').attr('disabled', false);
				$('#id_refine_time_window2, #id_refine_percent_applied2').closest('tr').hide();
				samFillScenarioValues(samScenarioInputs_chlorpyrifos_corn);
				cropsArray = cropsArray_corn;
				for (i=0;i<cropsArray.length;i++) {
					cropArrayGenerator(cropsArray[i]);
				}
				break;
			case '3':
				$(':input:not(#id_scenario_selection, :button)').attr('disabled', true);
				$('button.submit').attr('disabled', false);
				$('#id_refine_time_window2, #id_refine_percent_applied2').closest('tr').hide();
				samFillScenarioValues(samScenarioInputs_chlorpyrifos_soybeans);
				cropsArray = cropsArray_soybeans;
				for (i=0;i<cropsArray.length;i++) {
					cropArrayGenerator(cropsArray[i]);
				}
				break;
			case '4':
				$(':input:not(#id_scenario_selection, :button)').attr('disabled', true);
				$('button.submit').attr('disabled', false);
				$('#id_refine_time_window2, #id_refine_percent_applied2').closest('tr').show();
				samFillScenarioValues(samScenarioInputs_fipronil_corn);
				cropsArray = cropsArray_corn;
				for (i=0;i<cropsArray.length;i++) {
					cropArrayGenerator(cropsArray[i]);
				}
				break;
			case '5':
				$(':input:not(#id_scenario_selection, :button)').attr('disabled', true);
				$('button.submit').attr('disabled', false);
				$('#id_refine_time_window2, #id_refine_percent_applied2').closest('tr').show();
				samFillScenarioValues(samScenarioInputs_metolachlor_corn);
				cropsArray = cropsArray_corn;
				for (i=0;i<cropsArray.length;i++) {
					cropArrayGenerator(cropsArray[i]);
				}
				break;
			default:
				$(':input:not(#id_scenario_selection)').attr('disabled', false);
				$('button.submit').attr('disabled', true);
		}
	}

	$('#id_scenario_selection').change(function() {
			samFillScenarioCrops($(this).val());
	});

	// Selected Crops Rows
	function cropArrayGenerator(crop) {
		var scenario = $('#id_scenario_selection').val();
		if (crop_list_array.length < 4) {
			if ($('#crop1').text() == '') {
				if (scenario == '0') {
					$('#crop1').html(crop + " <span class='deleteCrop'>[x]</span>");
				}
				else {
					$('#crop1').html(crop);	
				}
				crop_list_array.push(crop);
			} else {
				if ($.inArray(crop, crop_list_array) == -1) {
					if (scenario == '0') {
						$('#crop1').closest('tr')
							.after('<tr><th></th><td>' + crop + " <span class='deleteCrop'>[x]</span>" + '</td></tr>');
					}
					else {
						$('#crop1').closest('tr')
							.after('<tr><th></th><td>' + crop + '</td></tr>');
					}
					crop_list_array.push(crop);
				}
			}
		}
		if (crop_list_array.length == 4) {
			$('#id_crop').prop('disabled', true);
		}
		$('#id_crop_number').val(crop_list_array.length);
	}
	$('#id_crop').change(function() {
		if ($(this).val() !== '0') {
			var crop = $("#id_crop option:selected").text();
			cropArrayGenerator(crop);
		}
	});
	function resetCropRows() {
		var tr1st = $('#crop1').closest('tr').index();
		var trLast = $('#id_crop_number').closest('tr').index();
		if (tr1st !== -1) {
			var noOfCrops = trLast - tr1st;
			if (noOfCrops > 1) {
				for (i=0; i<noOfCrops; i++) {
					if (i == 0) {
						$('#crop1').text('');
					}
					else {
						$('table.tab_Application tr').get(2).remove();
					}
				}
				$('#id_crop_number').val('0');
				crop_list_array = [];
			}
		}
	}
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

});