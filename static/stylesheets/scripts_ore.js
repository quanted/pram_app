$( document ).ready(function() {
	// Call function to setup tabbed nav
	uberNavTabs(
		['ToxInp', 'CropTargetSel', 'OccHandler'],
		{   "isSubTabs":true,
			"ToxInp": [".tab_tox_st", ".tab_tox_it", ".tab_tox_lt"] }
	);

	// Inital setup
	$('.tab_tox_st').show();
	$('.tab_tox_it, .tab_tox_lt, .tab_CropTargetSel, .tab_OccHandler').hide();
	$('#id_expDurationType_0').prop("checked",true);

	// Checkboxes
	var selectedArray = ["id_expDurationType_0"]  // default with Short-term selected
	$("input[name='expDurationType']").click(function() {
		var selection = $(this).attr('id');
		console.log(selection);
		arrayIndex = $.inArray(selection, selectedArray);
		if ( arrayIndex == -1) {
			selectedArray.splice(0, 0, selection);  // add selection to array
			switch(selection) {
				case 'id_expDurationType_0':
					$('.tab_tox_st').show();
					break;
				case 'id_expDurationType_1':
					$('.tab_tox_it').show();
					break;
				case 'id_expDurationType_2':
					$('.tab_tox_lt').show();
					break;
			}
		} else {
			selectedArray.splice(arrayIndex, 1);  // remove selection from array
			switch(selection) {
				case 'id_expDurationType_0':
					$('.tab_tox_st').hide();
					break;
				case 'id_expDurationType_1':
					$('.tab_tox_it').hide();
					break;
				case 'id_expDurationType_2':
					$('.tab_tox_lt').hide();
					break;
			}
		}

	});

	// NOT FINISHED
	$('.ToxInp').click(function() {
		if ( $.inArray('id_expDurationType_0', selectedArray) !== -1 ) {
			$('.tab_tox_it, .tab_tox_lt').hide();
			$('.tab_tox_st').show();
		} else if ( $.inArray('id_expDurationType_1', selectedArray) !== -1 ) {
			$('.tab_tox_st, .tab_tox_lt').hide();
			$('.tab_tox_it').show();
		} else if ( $.inArray('id_expDurationType_2', selectedArray) !== -1 ) {
			$('.tab_tox_st, .tab_tox_it').hide();
			$('.tab_tox_lt').show();
		}
	});

	// Crop-Target Lookup
	$('#id_group_no, #id_group_name, #id_subgroup_no, #id_subgroup_name, #id_crop_category').prop('disabled', true);
	var cropTargetFieldsArray = [];
	$('table.tab_CropTargetSel select').each(function() {
		cropTargetFieldsArray.push($(this).attr('id'));
	});
	var noOfCropTargetFields = cropTargetFieldsArray.length;
	$('table.tab_CropTargetSel select').change(function() {
		var curr_crop = $(this).val();
		for (var i = 0; i < noOfCropTargetFields; i++) {
			$('#'+cropTargetFieldsArray[i]).val(curr_crop);
		}
		var value = $('#id_crop_category option:selected').text();
		console.log(value);
		$('#id_exp_category').val(value);
		category_queury(value);
	});
	// $('#id_crop_category').change(function() {
	// 	var value = $(this).text();
	// 	console.log(value);
	// 	$('#id_exp_category').text(value);
	// });

	// Exposure Scenario
	function category_queury(crop_category) {
		$.ajax({
			url: "category",
			type: "POST",
			data: {'category': crop_category},
			success: function(json) { 
				console.log(json.result);

				var worker_activites = json.result[0];
				// $('#id_exp_worker_activity').val(worker_activites);
				create_checkboxes("worker_activity", worker_activites);

				var app_type = json.result[1];
				create_checkboxes("app_type", app_type);

				var app_equipment = json.result[2];
				create_checkboxes("app_equipment", app_equipment);

				var formulation = json.result[3];
				create_checkboxes("formulation", formulation);
				
			}
		});
	}

	function create_checkboxes(type, item_list) {


		console.log(item_list);

		var checkboxes = "<td><ul>";

		if (type !== 'formulation') {
			for (i = 0; i < item_list.length; i++) {
				checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label></li>"
			}
		} else {
			checkboxes = checkboxes + "<li style='text-align: right;'>Application Rate (lb ai/acre): </li>"
			for (i = 0; i < item_list.length; i++) {
				checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label><input class='formulation_rate' name='" + item_list[i] + " type='number'></li>"
			}
		}

		checkboxes = checkboxes + "</ul></td>"

		// $('#id_exp_' + type).replaceWith(checkboxes);
		$('label[for=id_exp_' + type + ']').closest('th').next().replaceWith(checkboxes);

	}

	// Enabled Crop-Target Category Lookup form fields before form submit
	// ***Not needed with how the fields are populated currently; must re-query DB after form submit***
	// $('.submit').click(function(e) {
	// 	e.preventDefault();
	// 	alert('Prevented!');
	// 	$('#id_group_no, #id_group_name, #id_subgroup_no, #id_subgroup_name, #id_crop_category').prop('disabled', false);
	// 	$('form').submit();
	// });

});