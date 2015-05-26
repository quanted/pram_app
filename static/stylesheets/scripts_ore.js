$( document ).ready(function() {
	// Call function to setup tabbed nav
	uberNavTabs(
		['ToxInp', 'CropTargetSel', 'OccHandler'],
		{   "isSubTabs":true,
			"ToxInp": [".tab_tox_st", ".tab_tox_it", ".tab_tox_lt"] }
	);

	// Initial setup
	$('.tab_tox_st').show();
	$('.tab_tox_it, .tab_tox_lt, .tab_CropTargetSel, .tab_OccHandler').hide();
	$('#id_expDurationType_0').prop("checked",true);
    $('#id_expComboType_0').prop("checked",true);
    $('input.submit.input_button').val('Filter');
    updateExposureScenario();

	// Checkboxes
	var selectedArray = ["id_expDurationType_0"];  // default with Short-term selected
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
    var cropCategory;
	$('table.tab_CropTargetSel select').change(function() {
		var curr_crop = $(this).val();
		for (var i = 0; i < noOfCropTargetFields; i++) {
			$('#'+cropTargetFieldsArray[i]).val(curr_crop);
		}
        updateExposureScenario();
	});

    // Get current Crop/Target Category and update Exposure Scenario tab
    function updateExposureScenario() {
        cropCategory = $('#id_crop_category option:selected').text();
        console.log(cropCategory);
		$('#id_exp_category').val(cropCategory);
		categoryQuery( { 'crop_category': cropCategory }, false );
	}

	// Exposure Scenario

	var sqlData;
	function categoryQuery(ore_object, update_checkboxes) {
		var key;
		$.ajax({
			url: "query/category",
			type: "POST",
			data: ore_object,
			success: function(json) { 
				console.log(json.result);
				sqlData = json.result;
				if (update_checkboxes) {
					for (key in sqlData) {
						if (sqlData.hasOwnProperty(key)) {
							if (ore_object.es_type !== key ||
								ore_object.es_type == 'Formulation') {
									updateCheckboxes(key, sqlData[key]);
							}
						}
					}
				} else {
					for (key in sqlData) {
						if (sqlData.hasOwnProperty(key)) {
							createCheckboxes(key, sqlData[key]);
						}
					}
				}
			}
		});
	}

	function createCheckboxes(type, item_list) {

        var checkboxes = "<td><ul id=" + type + ">";

		if (type == 'Formulation') {
			for (i = 0; i < item_list.length; i++) {
				checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label><input class='formulation_rate' name='" + item_list[i] + " type='number'></li>"
			}
		} else {
			for (i = 0; i < item_list.length; i++) {
				checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label></li>"
			}
		}

		checkboxes = checkboxes + "</ul></td>";

		$('label[for=id_exp_' + type + ']').closest('th').next().replaceWith(checkboxes);

	}

	function updateCheckboxes(type, item_list) {
		$('#' + type).children('li').each(function() {
			// Loop over each child of <li>, e.g. <input>
			var elem = $(this).find('input');
			if ($.inArray(elem.attr('name'), item_list) == -1) {
				elem.prop('checked', false);
				if (type == 'Formulation') {
					elem.closest('label').next('input').prop('disabled', true);
				}
			} else {
				elem.prop('checked', true);
				if (type == 'Formulation') {
					elem.closest('label').next('input').prop('disabled', false);
				}
			}
		});
	}

    var articlesWidth = $('.articles_output').width();
    var articlesHeight = $('.articles_output').height();
    var oreOutputDivLeft = (articlesWidth / 2) - 200;
    var oreOutputDivTop = (articlesHeight / 2) - 30;

	$('.submit').click(function(e) {
		e.preventDefault();

        $.ajax({
			url: "query/assess",
			type: "POST",
			data: {'category': crop_category},
			success: function(json) {
				console.log(json.result);

                $('#ore_output').html(
                    "<h3>asdf;lasdfsadfDSFJSDk</h3>"
                ).css({
                    "position": "absolute",
                    "top": oreOutputDivTop,
                    "left": oreOutputDivLeft,
                    "padding": "30px 20px",
                    "width": "400px",
                    "height": "60px",
                    "border": "0 none",
                    "border-radius": "4px",
                    "-webkit-border-radius": "4px",
                    "-moz-border-radius": "4px",
                    "box-shadow": "3px 3px 15px #333",
                    "-webkit-box-shadow": "3px 3px 15px #333",
                    "-moz-box-shadow": "3px 3px 15px #333"
                });

			}
		});
	});
    $('#ore_output').click(function() {

    });
    // Watch the '.tab_OccHandler' class for new items added to the DOM
    $('.tab_OccHandler').on('click', 'input.checkbox', function() {
        var checkboxUnselItems = [];
		$(this).each(function() {
			if (!$(this).is(':checked')) {
				checkboxUnselItems.push($(this).val());
			}
        });
        //console.log(checkboxUnselItems);
		var es_type = $(this).closest('ul').attr('id');
        categoryQuery({ 'crop_category': cropCategory,
                        'es_type': es_type,
                        'es_type_filter': checkboxUnselItems },
						true );
    });

});