$( document ).ready(function() {
	// Call function to setup tabbed nav
	uberNavTabs(
		['ToxInp', 'CropTargetSel', 'OccHandler'],
		{   "isSubTabs":true,
			"ToxInp": [".tab_tox_st", ".tab_tox_it", ".tab_tox_lt"] }
	);

	// Initial setup
	$('.tab_tox_st').show();
	$('.tab_tox_it, .tab_tox_lt, .tab_CropTargetSel, .tab_OccHandler, #ore_output').hide();
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
            checkboxes = checkboxes + "<li style='text-align: right'>Application Rate:</li>";
			for (i = 0; i < item_list.length; i++) {
				checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label><input class='formulation_rate' name='app_rate_" + item_list[i] + "' type='number'></li>"
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
                if (!elem.checked) { // Do not re-checked previously unchecked boxes
                    return;
                } else {
				    if (type == 'Formulation') {
					    elem.closest('label').next('input').prop('disabled', false);
                    }
				}
                elem.prop('checked', true);
			}
		});
	}

	$('.submit').click(function(e) {
		e.preventDefault();
        //var formData = createFormData();
        //console.log(JSON.stringify(formData));
        var formData = {'test': 'test_data'};

        $.ajax({
			url: "query/output",
			type: "POST",
			data: JSON.stringify(formData),
            contentType: "application/json; charset=utf-8",
			success: function(json) {
				//console.log(json.result);

                $('#ore_output').html(
                    "<h3>" + json + "</h3>"
                ).css({
                    "position": "absolute",
                    //"top": "50%",
                    //"left": "50%",
                    //'margin-left' : $('#ore_output').outerWidth()/2,
                    //'margin-top' : $('#ore_output').outerHeight()/2,
                    //"padding": "30px 20px",
                    //"width": "400px",
                    //"height": "60px",
                    "border": "0 none",
                    "border-radius": "4px",
                    "-webkit-border-radius": "4px",
                    "-moz-border-radius": "4px",
                    "box-shadow": "3px 3px 15px #333",
                    "-webkit-box-shadow": "3px 3px 15px #333",
                    "-moz-box-shadow": "3px 3px 15px #333"
                });
                $.fn.center = function () {
                   this.css("position","absolute");
                   this.css("top", ( $(window).height() - this.height() ) / 2  + "px");
                   this.css("left", ( $(window).width() - this.width() ) / 2 + "px");
                   return this;
                };
                $('#ore_output').center().fadeIn().on('click', 'table', function() {
                    $('#ore_output').fadeOut();
                });
			},
            error: function() {
                alert('Error');
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

    function createFormData() {
        var neededTables = ['tab_ToxInp', 'tab_tox_st', 'tab_tox_it', 'tab_tox_lt', 'tab_OccHandler'];
        var formulations = [], app_eqips = [], app_types = [], activities = [];
        var formData = {};
        $("form").find("table").each(function() {
            var className = $(this).attr('class').split(' ')[2]; // 3rd .class name
            if ($.inArray(className, neededTables) !== -1) {
                $(this).find('input, textarea, select').each(function() {
                    var inputType = this.tagName.toUpperCase() === "INPUT" && this.type.toUpperCase();
                    if (inputType !== "BUTTON" && inputType !== "SUBMIT") {
                        if (inputType == 'CHECKBOX') { // if checked = true, if not checked = false
                            if (className == 'tab_OccHandler') { // exp_scenario types
                                if ($(this).is(':checked')) {
                                    var exp_scenario = $(this).closest('ul').attr('id');
                                    switch(exp_scenario) { // Save checked items in arrays
                                        case 'Formulation':
                                            formulations.push(this.name);
                                            break;
                                        case 'AppEquip':
                                            app_eqips.push(this.name);
                                            break;
                                        case 'AppType':
                                            app_types.push(this.name);
                                            break;
                                        case 'Activity':
                                            activities.push(this.name);
                                            break;
                                    }
                                }
                            } else { // tox & exposure inputs
                                formData[this.name + '_' + $(this).val()] = !!$(this).is(':checked');
                            }
                        } else { // DOM name = input value
                            formData[this.name] = $(this).val();
                        }
                    }
                });
            }
            // Add checked item arrays to formData object
            formData['exp_scenario'] = {};
            formData['exp_scenario']['Formulation'] = formulations;
            formData['exp_scenario']['AppEquip'] = app_eqips;
            formData['exp_scenario']['AppType'] = app_types;
            formData['exp_scenario']['Activity'] = activities;
        });
        return formData;
    }

});