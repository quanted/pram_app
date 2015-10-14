$( document ).ready(function() {
	// Call function to setup tabbed nav
	uberNavTabs(
		['ToxInp', 'CropTargetSel', 'OccHandler'],
		{   "isSubTabs":true,
			"ToxInp": [".tab_tox_st", ".tab_tox_it", ".tab_tox_lt"] }
	);

	var returnObject;  // REST callback placeholder variable

	// Initial setup
	$('.tab_tox_st').show();
	$('.tab_tox_it, .tab_tox_lt, .tab_CropTargetSel, .tab_OccHandler, #ore_output').hide();
	$('#id_expDurationType_0').prop("checked",true);
    $('#id_expComboType_0').prop("checked",true);
    $('#id_expDurationType_0, #id_expDurationType_1, #id_expDurationType_2').prop('disabled', true);
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
        $('#id_exp_crop').val($('#id_crop_name option:selected').text());
		categoryQuery( { 'crop_category': cropCategory }, false );
	}

	// Exposure Scenario Tab
  var esTab = $('.tab_OccHandler');
	var sqlData;
	function categoryQuery(ore_object, update_checkboxes) {
    /*
    AJAX call to REST server to query the SQLite db using the attributes of the 'ore_object' parameter to filter the query.
    On success the UI is updated either creating the checkbox UI or updating it as determined by the 'update_checkboxes'
    Boolean parameter.

    param: ore_object, JS Object representing the 'checked' checkboxes for that es_type (e.g. Formulation)
    param: update_checkboxes, Boolean; dictate whether or not to update the UI based on SQLite query results
     */
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

  // Watch the '.tab_OccHandler' class (Exposure Scenario tab) for new items added to the DOM from createCheckboxes().
  esTab.on('click', 'input.checkbox', function() {
    /*
    When a checkbox is clicked on the Exposure Scenario tab, a JS Object is built representing all the checked
    checkboxes for that 'es_type' (e.g. Formulation).  The JS Object is sent to categoryQuery() to query the SQLite db
    and ultimately update the UI based on the query results.
     */
    var es_type = $(this).closest('ul');
    var es_type_name = es_type.attr('id');
    console.log(es_type_name);
    var checkboxSelectedItems = [];
    $(es_type).find('input.checkbox').each(function() {
      if ($(this).is(':checked')) {
        checkboxSelectedItems.push($(this).val());
      }
    });
    console.log(checkboxSelectedItems);
    categoryQuery({ 'crop_category': cropCategory,
                    'es_type': es_type_name,
                    'es_type_filter': checkboxSelectedItems },
        true );
  });

	function createCheckboxes(type, item_list) {
    /*
    Creates the actual checkbox HTML layout for the Exposure Scenario tab based on the results from categoryQuery().
     */
    var checkboxes = "<td><ul id=" + type + ">";
    var type_class = type.toLowerCase();
		if (type == 'Formulation') {
            checkboxes = checkboxes + "<li><input id='deselect_button' class='input_button' type='button' value='Deselect All'><span style='float: right'>Application rate (lb ai/acre):</span></li>";
			for (i = 0; i < item_list.length; i++) {
				checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox " + type_class + "' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label><input class='formulation_rate' name='app_rate_" + item_list[i] + "' type='number'></li>"
			}
		} else {
			for (i = 0; i < item_list.length; i++) {
				checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox " + type_class + "' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label></li>"
			}
		}
		checkboxes = checkboxes + "</ul></td>";
		$('label[for=id_exp_' + type + ']').closest('th').next().replaceWith(checkboxes);
	}

  var deselect_button_defValue = 'Deselect All';
  var deselect_button_altValue = 'Select All';
  esTab.on('click', 'input#deselect_button', function() {
    if (this.value == deselect_button_defValue) {
      // Deselect all Formulations
      esTab.find('input.formulation').each(function() {
        $(this).trigger('click');
      });
      this.value = deselect_button_altValue;
    } else {  // (this.value == deselect_button_altValue)
      esTab.find('input.checkbox').each(function () {
        $(this).prop('checked', true);
      });
      esTab.find('input.formulation_rate').each(function() {
        $(this).prop('disabled', false);
      });
      this.value = deselect_button_defValue;
    }
  });

	function updateCheckboxes(type, item_list) {
    /*
    Update checkboxes based on the results from categoryQuery().  Un-check checkbox if not available based on SQLite
    query results.  If type==Formulation, disable the the Application Rate input when un-checked.  Re-enable if re-checked.
    */
		$('#' + type).children('li').each(function() {  // Loop over each child of <li>, e.g. <input>
			var elem = $(this).find('input');
      if (!$(elem).is('input') || $(elem).attr('type') == 'button') {  // Make sure the 'elem' found is an 'input' elem and no a button
        return true;
      }
      var app_rate;
      if (elem.length > 1) {  // Formulation has two input fields, set elem to the first one (checkbox)
        app_rate = elem[1];
        elem = elem[0];
      }
			if ($.inArray($(elem).attr('name'), item_list) == -1 || item_list.length == 0) {  // Check if elem (e.g. Aerial) is in the SQL query; if not uncheck
				$(elem).prop('checked', false);
				if (type == 'Formulation') {
					$(app_rate).prop('disabled', true);
				}
			} else {  // Elem IS in the SQL query; therefore, it should be checked.  Also, Application Rate should be enabled.
        if (!$(elem).prop('checked')) {  // Do not re-checked previously unchecked boxes
          return;
        } else {  // Checkbox is checked.  If it's a Formulation re-enable the Application Rate input.
          if (type == 'Formulation') {
            $(app_rate).prop('disabled', false);
          }
				}
        $(elem).prop('checked', true);  // Set elem to checked (IS THIS NECESSARY???)
			}
		});
	}

	$('.submit').click(function(e) {
		e.preventDefault();
      var data = createFormData();
      console.log(data);
      if (data != null) {
        //console.log(JSON.stringify(data));
        $.ajax({
          url: "query/output",
          type: "POST",
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          success: function(json) {
            console.log(json);
            returnObject = json;
            $('#ore_output').html(
                "<div id='ore_output_x'></div>" + json.html
            ).css({
                "position": "absolute",
                "max-height": $(document).height() - 40 + "px"
              });
            $('.ore_output_table_container').css({
                "position": "relative",
                "background": "#F4F7ED",
                "border": "0 none",
                "border-radius": "4px",
                "padding": "8px",
                "overflow": "auto",
                "-webkit-border-radius": "4px",
                "-moz-border-radius": "4px",
                "box-shadow": "3px 3px 15px #333",
                "-webkit-box-shadow": "3px 3px 15px #333",
                "-moz-box-shadow": "3px 3px 15px #333"
            });
            $.fn.center = function () {
               this.css("top", ( $(window).height() - this.height() ) / 2  + "px");
               this.css("left", ( $(window).width() - this.width() ) / 2 + "px");
               return this;
            };
            $('#ore_output').center().fadeIn().on('click', 'div#ore_output_x', function() {
                $('#ore_output').fadeOut();
            });
            $('#ore_output_x').css({
              "cursor": "pointer",
              "z-index": "999999",
              "top": "16px",
              "left": ($('#ore_output').width() / 2) + "px"
            });
            $('#ore_output').center().fadeIn().on('click', 'input#export_button', exportToExcel);  // Bind exportToExcel() to 'input#export_button'
          },
          error: function() {
            alert('Error');
          }
        });
      }
	});

  // Export to Excel Spreadsheet
  function exportToExcel() {

  //// Create FormData object to populate with returnObject key-values
  //console.log(returnObject);
  //var formData = new FormData();
  //for (var key in returnObject) {
  //  console.log(key + ": " + returnObject.key)
  //}
  //$.each(returnObject.output, function(key, value) {
  //  //console.log( key + ": " + value );
  //  $.each(value, function(k, v) { // Each output "row" / object shown in Output Table
  //    formData.append(value.activity + '.' + value.app_equip + '.' + k, v);
  //  });
  //});
  //var request = new XMLHttpRequest();
  //request.open("POST", "export");
  //request.send(formData);

    // Button animation
    var elem = $('#export_button');
    var width = elem.width();
    elem.animate({'color': 'rgba(0,0,0,0.0)'}, 300, function() {  // Fade text to transparent
    	elem.width(width).animate({'color': 'rgba(0,0,0,1)'}, 300, function() {  // Change text and fade back to visible
        //$('#ore_output').off('click', 'input#export_button', exportToExcel);  // Unbind this function to button click
      });
    });

    // Submit 'returnObject' data to create spreadsheet
    $.ajax({
      url: "export",
      type: "POST",
      data: JSON.stringify(returnObject),
      contentType: "application/json; charset=utf-8",
      success: function (json) {
        if (json.error) {
          alert('Error: ' + json.error);
        } else {
          if (json.link && json.link != '') {
            downloadXlsx(json.link);
          }
        }
      }
    });
  }

  function downloadXlsx(link) {
    $('form#get_xlsx').attr({'action': 'download', 'method': 'POST'})
      .html("<input type='hidden' name='link' value='" + link + "'></input>").submit();
  }

  function createFormData() {
    // Manually generates a JS Object of form data to POST to via AJAX call
      var neededTables = ['tab_ToxInp', 'tab_tox_st', 'tab_tox_it', 'tab_tox_lt', 'tab_OccHandler'];
      var formulations = [], app_eqips = [], app_types = [], activities = [];
      var formData = {};
      formData.app_rate = {};
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
                          if ($(this).attr('class') == 'formulation_rate') {
                              if (!this.disabled) {  // only check app_rate value if field is not disabled
                                  if ($.isNumeric($(this).val())) {
                                      formData.app_rate[this.name] = $(this).val();
                                  } else {
                                      alert("Must enter Application Rate value for " + this.name + " formulation");
                                      return formData = null;  // exit function, and return formData as null bc it is invalid
                                  }
                              }
                          } else {
                              if (this.name == 'expComboType') {
                                  if (this.checked) {  //  only put checked Radio Button into formData
                                      formData[this.name] = $(this).val();
                                  }
                              } else {
                                  formData[this.name] = $(this).val();
                              }
                          }
                      }
                  }
              });
          }
          if (formData != null) {  // Add checked item arrays to valid formData object
              formData.exp_scenario = {};
              formData.exp_scenario.Formulation = formulations;
              formData.exp_scenario.AppEquip = app_eqips;
              formData.exp_scenario.AppType = app_types;
              formData.exp_scenario.Activity = activities;
          }
      });  // End of ".each()" loop
      console.log(formulations.length, app_eqips.length, app_types.length, activities.length);
      var submitValidateAlert = "Please select at least one ";
      if (formulations.length == 0) {alert(submitValidateAlert + "Formulation"); return formData = null;}
      if (app_eqips.length == 0) {alert(submitValidateAlert + "Application Equipment"); return formData = null;}
      if (app_types.length == 0) {alert(submitValidateAlert + "Application Type"); return formData = null;}
      if (activities.length == 0) {alert(submitValidateAlert + "Worker Activity"); return formData = null;}
      return formData;
  }

});