$(document).ready(function () {
  // Call function to setup tabbed nav
  uberNavTabs(
    ['ToxInp', 'CropTargetSel', 'OccHandler'],
    {
      "isSubTabs": true,
      "ToxInp": [".tab_tox_st", ".tab_tox_it", ".tab_tox_lt"]
    }
  );

  var returnObject;  // REST callback placeholder variable

  // Initial setup
  $('.tab_tox_st').show();
  $('.tab_tox_it, .tab_tox_lt, .tab_CropTargetSel, .tab_OccHandler, #ore_output').hide();
  $('#id_expDurationType_0, #id_expComboType_0').prop("checked", true);
  $('#id_expDurationType_0, #id_expDurationType_1, #id_expDurationType_2').prop('disabled', true);
  updateExposureScenario();

  // Checkboxes
  var selectedArray = ["id_expDurationType_0"];  // default with Short-term selected
  $("input[name='expDurationType']").click(function () {
    var selection = $(this).attr('id');
    console.log(selection);
    arrayIndex = $.inArray(selection, selectedArray);
    if (arrayIndex == -1) {
      selectedArray.splice(0, 0, selection);  // add selection to array
      switch (selection) {
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
      switch (selection) {
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
  $('.ToxInp').click(function () {
    if ($.inArray('id_expDurationType_0', selectedArray) !== -1) {
      $('.tab_tox_it, .tab_tox_lt').hide();
      $('.tab_tox_st').show();
    } else if ($.inArray('id_expDurationType_1', selectedArray) !== -1) {
      $('.tab_tox_st, .tab_tox_lt').hide();
      $('.tab_tox_it').show();
    } else if ($.inArray('id_expDurationType_2', selectedArray) !== -1) {
      $('.tab_tox_st, .tab_tox_it').hide();
      $('.tab_tox_lt').show();
    }
  });

  // Crop-Target Lookup
  $('#id_group_no, #id_group_name, #id_subgroup_no, #id_subgroup_name, #id_crop_category').prop('disabled', true);
  var cropTargetFieldsArray = [];
  $('table.tab_CropTargetSel select').each(function () {
    cropTargetFieldsArray.push($(this).attr('id'));
  });
  var noOfCropTargetFields = cropTargetFieldsArray.length;
  var cropCategory;
  $('table.tab_CropTargetSel select').change(function () {
    var curr_crop = $(this).val();
    for (var i = 0; i < noOfCropTargetFields; i++) {
      $('#' + cropTargetFieldsArray[i]).val(curr_crop);
    }
    updateExposureScenario();
  });

  // Get current Crop/Target Category and update Exposure Scenario tab
  function updateExposureScenario() {
    cropCategory = $('#id_crop_category option:selected').text();
    console.log(cropCategory);
    $('#id_exp_category').val(cropCategory);
    $('#id_exp_crop').val($('#id_crop_name option:selected').text());
    categoryQuery({'crop_category': cropCategory}, false);
  }

  // Exposure Scenario Tab
  var esTab = $(".tab_OccHandler");
  var sqlData;

  function categoryQuery(ore_object, update_checkboxes) {
    /*
     AJAX call to REST server to query the SQLite db using the attributes of the 'ore_object' parameter to filter the
     query. On success the UI is updated either creating the checkbox UI or updating it as determined by the
     'update_checkboxes' Boolean parameter.

     param: ore_object, JS Object representing the 'checked' checkboxes for that es_type (e.g. Formulation)
     param: update_checkboxes, Boolean; dictate whether or not to update the UI based on SQLite query results
     */
    $.ajax({
      url: "query/category",
      type: "POST",
      data: ore_object,
      success: function (json) {
        console.log(json.result);
        sqlData = json.result;
        if (update_checkboxes) {
          updateCheckboxesPreFilter(ore_object.es_type, sqlData);
          //for (key in sqlData) {
          //}
        }
        else {
          for (var key in sqlData) {
            if (sqlData.hasOwnProperty(key)) {
              createCheckboxes(key, sqlData[key]);
            }
          }
        }
      }
    });
  }

  // Watch the '.tab_OccHandler' class (Exposure Scenario tab) for new items added to the DOM from createCheckboxes().
  esTab.on('click', 'input.checkbox', function () {
    /*
     When a checkbox is clicked on the Exposure Scenario tab, a JS Object is built representing all the checked
     checkboxes for that 'es_type' (e.g. Formulation).  The JS Object is sent to categoryQuery() to query the SQLite db
     and ultimately update the UI based on the query results.
     */
    var es_type = $(this).closest('ul');
    var es_type_name = es_type.attr('id');
    console.log(es_type_name);
    var checkboxSelectedItems = [];
    $(es_type).find('input.checkbox').each(function () {
      if ($(this).is(':checked')) {
        checkboxSelectedItems.push($(this).val());
      }
    });
    console.log(checkboxSelectedItems);
    categoryQuery({
        'crop_category': cropCategory,
        'es_type': es_type_name,
        'es_type_filter': checkboxSelectedItems
      },
      true
    );
  });

  esTab.on('click', 'input.toAppEquip', function () {
    $(this).slideUp();
    $('#table_AppEquip').show();
  });

  esTab.on('click', 'input.toAppType', function () {
    $(this).slideUp();
    $('#table_AppType').show();
  });

  esTab.on('click', 'input.toActivity', function () {
    $(this).slideUp();
    $('#table_Activity').show();
  });

  //function createCheckboxes(type, item_list) {
  // /*
  // Creates the checkbox HTML DOM layout for the Exposure Scenario tab based on the results from categoryQuery().
  //  */
  // var checkboxes = "<td><ul id=" + type + ">";
  // var type_class = type.toLowerCase();
  //	if (type == 'Formulation') {
  //     checkboxes = checkboxes + "<li><input id='deselect_button' class='input_button' type='button' value='Deselect All'><span style='float: right'>Application rate:</span></li>";
  //		for (var i = 0; i < item_list.length; i++) {
  //			checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox " + type_class + "' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label><span style='float: right; margin-left: 6px'> unit</span><input class='formulation_rate' name='app_rate_" + item_list[i] + "' type='number'></li>"
  //		}
  //   checkboxes = checkboxes + "</ul><input type='button' class='toAppEquip input_button' value='Choose Application Equipment...'></td>";
  //	} else {
  //		for (var i = 0; i < item_list.length; i++) {
  //			checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox " + type_class + "' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label></li>"
  //		}
  //   checkboxes = checkboxes + "</ul>"
  //   switch (type) {
  //     case "AppEquip":
  //       checkboxes = checkboxes + "<input type='button' class='toAppType input_button' value='Choose Application Type...'>"
  //       break;
  //     case "AppType":
  //       checkboxes = checkboxes + "<input type='button' class='toActivity input_button' value='Choose Worker Activities...'>"
  //       break;
  //   }
  //   checkboxes = checkboxes + "</td>";
  //	}
  //	$('label[for=id_exp_' + type + ']').closest('th').next().replaceWith(checkboxes);
  //}
  function createCheckboxes(type, item_list) {
    /*
     Creates the checkbox HTML DOM layout for the Exposure Scenario tab based on the results from categoryQuery().
     */
    var checkboxes = "<td><ul id=" + type + ">";
    var type_class = type.toLowerCase();
    if (type == 'Formulation') {
      checkboxes = checkboxes + "<li><input id='deselect_button' class='input_button' type='button' value='Deselect All'><span style='float: right'>Application rate:</span></li>";
      for (var i = 0; i < item_list.length; i++) {
        checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox " + type_class + "' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label><span style='float: right; margin-left: 6px'> unit</span><input class='formulation_rate' name='app_rate_" + item_list[i] + "' type='number'></li>"
      }
      checkboxes = checkboxes + "</ul><input type='button' class='toAppEquip input_button' value='Choose Application Equipment...'></td>";
    } else {
      for (var i = 0; i < item_list.length; i++) {
        checkboxes = checkboxes + "<li><label for='id_" + item_list[i] + "'><input type='checkbox' class='checkbox " + type_class + "' id='id_" + item_list[i] + "' name='" + item_list[i] + "' value='" + item_list[i] + "' checked='checked'>" + item_list[i] + "</label></li>"
      }
      checkboxes = checkboxes + "</ul>";
      switch (type) {
        case "AppEquip":
          checkboxes = checkboxes + "<input type='button' class='toAppType input_button' value='Choose Application Type...'>";
          break;
        case "AppType":
          checkboxes = checkboxes + "<input type='button' class='toActivity input_button' value='Choose Worker Activities...'>";
          break;
      }
      checkboxes = checkboxes + "</td>";
    }
    $('table#table_' + type + ' td').replaceWith(checkboxes);
  }

  var deselect_button_defValue = 'Deselect All';
  var deselect_button_altValue = 'Select All';
  esTab.on('click', 'input#deselect_button', function () {
    if (this.value == deselect_button_defValue) {
      // Deselect all Formulations
      esTab.find('input.formulation').each(function () {
        $(this).trigger('click');
      });
      this.value = deselect_button_altValue;
    } else {  // (this.value == deselect_button_altValue)
      esTab.find('input.checkbox').each(function () {
        $(this).prop('checked', true);
      });
      esTab.find('input.formulation_rate').each(function () {
        $(this).prop('disabled', false);
      });
      this.value = deselect_button_defValue;
    }
  });


  function updateCheckboxesPreFilter(es_type_clicked, data) {
    $.each(data, function (es_type, checkbox) {
      //console.log(es_type_clicked, es_type, checkbox)
      switch (es_type_clicked) {
        case "Formulation":
          // Updates AppEquip, AppType & Activity
          console.log("Formulation");
          if (es_type == "Formulation" || es_type == "AppEquip" || es_type == "AppType" || es_type == "Activity") {
            // Must send the "Formulation" clicks here too so the App. Rate text inputs can be disabled
            updateCheckboxes(es_type_clicked, es_type, checkbox)
          }
          break;
        case "AppEquip":
          // Updates AppType & Activity
          console.log("AppEquip");
          if (es_type == "AppType" || es_type == "Activity") {
            updateCheckboxes(es_type_clicked, es_type, checkbox)
          }
          break;
        case "AppType":
          // Updates Activity
          console.log("AppType");
          if (es_type == "Activity") {
            updateCheckboxes(es_type_clicked, es_type, checkbox)
          }
          break;
        case "Activity":
          // Worker Activity does not update any sections
          console.log("Activity");
          break;
      }
    });
  }

  function updateCheckboxes(es_type_clicked, es_type, item_list) {
    /*
     Update checkboxes based on the results from categoryQuery().  Un-check checkbox if not available based on SQLite
     query results.

     # TODO: Remove the next line if I change the code logic here for the "Top-Down" logic approach
     If type==Formulation, disable the the Application Rate input when un-checked.  Re-enable if re-checked.
     */
    $('#' + es_type).children('li').each(function () {  // Loop over each child of <li>, e.g. <input>
      var elem = $(this).find('input');
      if (!$(elem).is('input') || $(elem).attr('type') == 'button') {  // Make sure the 'elem' found is an 'input' elem and not a button
        return true;
      }
      var app_rate;
      if (elem.length > 1) {  // Formulation has two input fields, set elem to the first one (checkbox)
        app_rate = elem[1];
        elem = elem[0];
      }
      if ($.inArray($(elem).attr('name'), item_list) == -1 || item_list.length == 0) {  // if elem IS NOT in the SQL query, it should be un-checked
        if (es_type == 'Formulation') {  // Formulations NOT in the SQL query should disable their app_rate input box
          $(app_rate).prop('disabled', true);
          $(elem).prop('checked', false);
        }
        else {
          $(elem).prop({'checked': false, 'disabled': true});
        }
      }
      else {  // else if elem IS in the SQL query, it should be checked & enabled.  Also, app_rate should be enabled.
        $(elem).prop('disabled', false);
        if (!$(elem).prop('checked')) {  // Do not re-checked previously unchecked boxes (exit this logic)
          //$(elem).prop('disabled', false);
          //return;
        }
        else {  // Checkbox is checked.  If it's a Formulation re-enable the Application Rate input.
          if (es_type_clicked == 'Formulation') {
            $(app_rate).prop('disabled', false);
          }
          else {
            if (!$(elem).prop('checked')) {
              $(elem).prop('disabled', false);
            }
          }
        }
        $(elem).prop('checked', true);
      }
    });
  }

  $('.submit').click(function (e) {
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
        success: function (json) {
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
            this.css("top", ( $(window).height() - this.height() ) / 2 + "px");
            this.css("left", ( $(window).width() - this.width() ) / 2 + "px");
            return this;
          };
          $('#ore_output').center().fadeIn().on('click', 'div#ore_output_x', function () {
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
        error: function () {
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
    elem.animate({'color': 'rgba(0,0,0,0.0)'}, 300, function () {  // Fade text to transparent
      elem.width(width).animate({'color': 'rgba(0,0,0,1)'}, 300, function () {  // Change text and fade back to visible
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
      .html("<input type='hidden' name='link' value='" + link + "'>").submit();
  }

  function createFormData() {
    // Manually generates a JS Object of form data to POST via AJAX call to backend server
    var neededTables = ['tab_ToxInp', 'tab_tox_st', 'tab_tox_it', 'tab_tox_lt', 'tab_OccHandler'];
    var formulations = [], app_eqips = [], app_types = [], activities = [];
    var formData = {};
    formData.app_rate = {};
    $("form").find("table").each(function () {
      try {
        var className = $(this).attr('class').split(' ')[2]; // 3rd .class name
        if ($.inArray(className, neededTables) !== -1) {
          $(this).find('input, textarea, select').each(function () {
            var inputType = this.tagName.toUpperCase() === "INPUT" && this.type.toUpperCase();
            if (inputType !== "BUTTON" && inputType !== "SUBMIT") {
              if (inputType == 'CHECKBOX') { // if checked = true, if not checked = false
                if (className == 'tab_OccHandler') { // exp_scenario types
                  if ($(this).is(':checked')) {
                    var exp_scenario = $(this).closest('ul').attr('id');
                    switch (exp_scenario) { // Save checked items in arrays
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
                      var appRateBox = $("input[name='"+ this.name +"']");
                      var formulationName = $('#id_' + appRateBox.attr('name').replace('/', '\\/').split('_')[2]).val();
                      //console.log(formulationName.replace('/', '\\/'));
                      alert("Must enter Application Rate value for " + formulationName + " formulation");
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
      }
      catch(err) {}
      if (formData != null) {  // Add checked item arrays to valid formData object
        formData.exp_scenario = {};
        formData.exp_scenario.Formulation = formulations;
        formData.exp_scenario.AppEquip = app_eqips;
        formData.exp_scenario.AppType = app_types;
        formData.exp_scenario.Activity = activities;
      }
    });  // End of ".each()" loop

    // Input validation
    var submitValidateAlert = "Please select at least one ";
    if (formulations.length == 0) {
      alert(submitValidateAlert + "Formulation");
      return formData = null;
    }
    if (app_eqips.length == 0) {
      alert(submitValidateAlert + "Application Equipment");
      return formData = null;
    }
    if (app_types.length == 0) {
      alert(submitValidateAlert + "Application Type");
      return formData = null;
    }
    if (activities.length == 0) {
      alert(submitValidateAlert + "Worker Activity");
      return formData = null;
    }
    return formData;
  }

});