import StringIO
import logging
import os
import shutil
import string
import random
import sys

__author__ = 'jflaisha'

import xlsxwriter
import ore_xls_formatter


class OreXls(object):
    def __init__(self, xlsx, ore_obj):
        # self.wb = xlsxwriter.Workbook(xlsx, {'in_memory': True})  # Create Workbook in-memory
        self.wb = xlsxwriter.Workbook(xlsx)
        self.ws_tox_expo = self.wb.add_worksheet('TOX and EXPO INPUTS')
        self.ws_crop_target = self.wb.add_worksheet('Crop-Target Category Lookup')
        self.ws_occ_handler = self.wb.add_worksheet('OccHndler_Non-cancer')

        self.ore_obj = ore_obj

        # Generate Format objects
        self.default_format = self.gen_default_format()
        self.merge_format = self.gen_merge_format()
        self.merge_format_gray = self.gen_merge_format_gray()
        self.green_format = self.gen_green_format()

    def close(self):
        self.wb.close()

    def gen_default_format(self):
        self.default_format_dict = {
            'border': 1,
            'valign': 'vcenter',
            'text_wrap': 1}
        return self.wb.add_format(self.default_format_dict)

    def gen_merge_format(self):
        self.merge_format_dict = self.default_format_dict.copy()
        self.merge_format_dict['align'] = 'center'
        self.merge_format_dict['bold'] = 1
        return self.wb.add_format(self.merge_format_dict)

    def gen_merge_format_gray(self):
        gray_format_dict = self.merge_format_dict.copy()
        gray_format_dict['fg_color'] = '#D9D9D9'
        return self.wb.add_format(gray_format_dict)

    def gen_green_format(self):
        green_format_dict = self.default_format_dict.copy()
        green_format_dict['fg_color'] = '#C4D79B'
        green_format_dict['bold'] = 0
        return self.wb.add_format(green_format_dict)

    def tox_expo_inputs_sheet(self):
        """
        Generate the TOX and EXPO INPUTS sheet
        """

        # Format worksheet
        self.ws_tox_expo.set_column('B:B', 16)
        self.ws_tox_expo.set_column('C:C', 22)
        self.ws_tox_expo.set_column('D:D', 40)
        self.ws_tox_expo.set_column('E:E', 32)
        self.ws_tox_expo.set_row(5, 32)

        # Instantiate worksheet properties
        tox_inputs_chem = ToxExpoInputChemicalLabels()
        tox_inputs_tox = ToxExpoInputToxicityLabels()
        tox_inputs_bw = ToxExpoInputBodyWeightLabels()

        # Chemical Info
        self.ws_tox_expo.merge_range('B2:D2', tox_inputs_chem.chemical_info, self.merge_format_gray)
        self.ws_tox_expo.merge_range('B4:D4', tox_inputs_chem.active_ingredient, self.merge_format_gray)
        self.ws_tox_expo.merge_range('B6:D6', tox_inputs_chem.exp_duration, self.merge_format_gray)

        # Toxicity
        self.ws_tox_expo.merge_range('B8:E8', tox_inputs_tox.toxicity_header, self.merge_format_gray)
        # Dermal
        self.ws_tox_expo.merge_range('B9:B13', tox_inputs_tox.dermal, self.merge_format)
        # Dermal - non-cancer
        self.ws_tox_expo.merge_range('C9:C11', tox_inputs_tox.non_cancer, self.merge_format)
        # Dermal - absorption
        self.ws_tox_expo.merge_range('C12:C13', tox_inputs_tox.absorption, self.merge_format)
        # Inhalation
        self.ws_tox_expo.merge_range('B14:B21', tox_inputs_tox.inhalation, self.merge_format)
        # Inhalation - non-cancer
        self.ws_tox_expo.merge_range('C14:C19', tox_inputs_tox.non_cancer, self.merge_format)
        # Inhalation - absorption
        self.ws_tox_expo.merge_range('C20:C21', tox_inputs_tox.absorption, self.merge_format)

        _item_list = ["pod_source", "loc", "abs_fraction", "abs_source"]
        i = 0

        _item_list.insert(0, "pod")
        for item in _item_list:
            self.ws_tox_expo.write_string(8 + i, 3, getattr(tox_inputs_tox, item), self.default_format)
            i += 1

        i = 0
        for item in ["inhal_oral", "inhal_hec_83", "inhal_hec_167", "inhal_hec_29"]:
            self.ws_tox_expo.write_string(13 + i, 3, tox_inputs_tox.pod + getattr(tox_inputs_tox, item), self.default_format)
            i += 1

        _item_list.remove("pod")
        i = 0
        for item in _item_list:
            self.ws_tox_expo.write_string(17 + i, 3, getattr(tox_inputs_tox, item), self.default_format)
            i += 1

        # Body Weight
        self.ws_tox_expo.merge_range('B23:E23', tox_inputs_bw.bw_header, self.merge_format_gray)
        self.ws_tox_expo.write_string('B24', tox_inputs_bw.dermal, self.merge_format_gray)
        self.ws_tox_expo.write_string('B25', tox_inputs_bw.inhalation, self.merge_format_gray)
        self.ws_tox_expo.merge_range('C24:C25', tox_inputs_bw.non_cancer, self.merge_format_gray)
        self.ws_tox_expo.merge_range('D24:D25', tox_inputs_bw.adults, self.default_format)

    def crop_target_sheet(self):
        """
        Generate the Crop-Target Category Lookup sheet
        """

        # Format worksheet
        self.ws_crop_target.set_column('A:A', 44)
        self.ws_crop_target.set_column('B:B', 22)
        self.ws_crop_target.set_column('C:C', 28)
        self.ws_crop_target.set_column('D:D', 28)
        self.ws_crop_target.set_column('E:E', 36)
        self.ws_crop_target.set_column('F:F', 36)

        # Instantiate worksheet properties
        crop_target = CropTargetLabels()

        # Fill label cells
        self.ws_crop_target.merge_range('A1:A4', crop_target.crop, self.merge_format_gray)
        self.ws_crop_target.merge_range('B1:E1', crop_target.tolerance_group, self.merge_format_gray)
        self.ws_crop_target.merge_range('B2:B4', crop_target.group, self.merge_format_gray)
        self.ws_crop_target.merge_range('C2:C4', crop_target.group_name, self.merge_format_gray)
        self.ws_crop_target.merge_range('D2:D4', crop_target.sub_group, self.merge_format_gray)
        self.ws_crop_target.merge_range('E2:E4', crop_target.sub_group_name, self.merge_format_gray)
        self.ws_crop_target.merge_range('F1:F4', crop_target.crop_target, self.merge_format_gray)

    def occ_handler_sheet_inputs(self):
        """
        Generate the inputs (column A - G) for the OccHndler_Non-cancer sheet
        """

        # Format worksheet
        self.ws_occ_handler.set_column('A:A', 18)
        self.ws_occ_handler.set_column('B:B', 18)
        self.ws_occ_handler.set_column('C:C', 18)
        self.ws_occ_handler.set_column('D:D', 18)
        self.ws_occ_handler.set_column('E:E', 24)
        self.ws_occ_handler.set_column('F:F', 10)
        self.ws_occ_handler.set_column('G:G', 10)
        self.ws_occ_handler.set_column('H:H', 10)
        self.ws_occ_handler.set_column('I:I', 10)

        # Instantiate worksheet properties
        occ_handler_in = OccHandlerNonCancerInputsLabels()
        occ_handler_out = OccHandlerNonCancerOutputsLabels()

        # Input labels
        self.ws_occ_handler.merge_range('A1:D1', occ_handler_in.exp_scenario, self.merge_format_gray)
        self.ws_occ_handler.write_string('A2', occ_handler_in.worker, self.merge_format_gray)
        self.ws_occ_handler.write_string('B2', occ_handler_in.formulation, self.merge_format_gray)
        self.ws_occ_handler.write_string('C2', occ_handler_in.app_equip, self.merge_format_gray)
        self.ws_occ_handler.write_string('D2', occ_handler_in.app_type, self.merge_format_gray)
        self.ws_occ_handler.merge_range('E1:E2', occ_handler_in.crop_target, self.merge_format_gray)
        self.ws_occ_handler.merge_range('F1:G1', occ_handler_in.app_rate, self.merge_format_gray)
        self.ws_occ_handler.write_string('F2', occ_handler_in.app_rate_value, self.merge_format_gray)
        self.ws_occ_handler.write_string('G2', occ_handler_in.app_rate_unit, self.merge_format_gray)

        # Output Lables
        self.ws_occ_handler.merge_range('H1:I1', occ_handler_out.area_treated, self.merge_format_gray)
        self.ws_occ_handler.write_string('H2', occ_handler_out.area_treated_value, self.merge_format_gray)
        self.ws_occ_handler.write_string('I2', occ_handler_out.area_treated_unit, self.merge_format_gray)

        def write_output_labels(header_label, label_list, start_col):
            """

            """
            no_of_cols = len(label_list)
            end_col = start_col + (no_of_cols - 1)
            # Write Header
            row = 0
            self.ws_occ_handler.merge_range(row, start_col, row, end_col, header_label, self.merge_format_gray)
            # Write PPE Labels
            row = 1
            col_counter = 0
            for label in label_list:
                self.ws_occ_handler.write(row, start_col + col_counter, label, self.merge_format_gray)
                col_counter += 1

        dermal_labels = occ_handler_out.get_dermal_ppe_labels()
        inhal_labels = occ_handler_out.get_inhal_ppe_labels()
        write_output_labels(occ_handler_out.dermal_unit_exp, dermal_labels, 9)
        write_output_labels(occ_handler_out.inhal_unit_exp, inhal_labels, 15)
        write_output_labels(occ_handler_out.dermal_exp, dermal_labels, 19)
        write_output_labels(occ_handler_out.dermal_dose, dermal_labels, 25)
        write_output_labels(occ_handler_out.dermal_moe, dermal_labels, 31)
        write_output_labels(occ_handler_out.inhal_exp, inhal_labels, 37)
        write_output_labels(occ_handler_out.inhal_dose, inhal_labels, 41)
        write_output_labels(occ_handler_out.inhal_moe, inhal_labels, 45)
                                                                    # 49

    def tox_expo_sheet_user(self):

        def determine_exp_duration(st=False, it=False, lt=False):
            """
            ONLY ST (SHORT-TERM) IS USED NOW
            """
            exp_duration = 'Short-term'
            suffix = '_st'

            return exp_duration, suffix

        exp_duration = determine_exp_duration(  self.ore_obj.input['expDurationType_st'],
                                                self.ore_obj.input['expDurationType_it'],
                                                self.ore_obj.input['expDurationType_lt'] )
        suffix = exp_duration[1]

        tox_expo_tab = ore_xls_formatter.OreXlsToxExpo(
            self.ore_obj.input['activeIngredient'],
            exp_duration[0],
            self.ore_obj.input['dermal_NC_POD' + suffix],
            self.ore_obj.input['inhalation_NC_POD_source' + suffix],
            self.ore_obj.input['dermal_NC_LOC' + suffix],
            self.ore_obj.input['dermal_abs_frac' + suffix],
            self.ore_obj.input['dermal_abs_source' + suffix],
            self.ore_obj.input['inhalation_NC_POD' + suffix],
            self.ore_obj.input['inhalation_NC_POD_HEC83' + suffix],
            self.ore_obj.input['inhalation_NC_POD_HEC167' + suffix],
            self.ore_obj.input['inhalation_NC_POD_HEC29' + suffix],
            self.ore_obj.input['inhalation_NC_POD_source' + suffix],
            self.ore_obj.input['inhalation_NC_LOC' + suffix],
            self.ore_obj.input['inhalation_abs_frac' + suffix],
            self.ore_obj.input['inhalation_abs_source' + suffix],
            self.ore_obj.input['bw_inhalation_NC' + suffix],
            self.ore_obj.input['bw_dermal_NC' + suffix]
        )
        ordered_attrs = tox_expo_tab.get_attrs()

        self.ws_tox_expo.write('E4', ordered_attrs[0])
        self.ws_tox_expo.write('E6', ordered_attrs[1])

        i = 2  #  Start at index=2 because items 0-1 are used above
        while i < (len(ordered_attrs) - 2):  # len() - 2 because the last two items are used outside of the loop
            self.ws_tox_expo.write(i + 8, 4, ordered_attrs[i])
            i += 1

        self.ws_tox_expo.write('E24', ordered_attrs[15])
        self.ws_tox_expo.write('E25', ordered_attrs[16])


    def crop_target_sheet_user(self):
        # TODO: This only works for 1 crop chosen.  Multiple crops will be implemented later.
        crop_target_tab = ore_xls_formatter.OreXlsCropTarget(
            #  crop, group_no, group_name, subgroup_no, subgroup_name, crop_target
            self.ore_obj.input['exp_crop'],
            'null',  # self.ore_obj.input[''],
            'null',  # self.ore_obj.input[''],
            'null',  # self.ore_obj.input[''],
            'null',  # self.ore_obj.input[''],
            self.ore_obj.input['exp_category']
        )
        ordered_attrs = crop_target_tab.get_attrs()
        i = 0
        while i < len(ordered_attrs):
            self.ws_crop_target.write(4, i, ordered_attrs[i])
            i += 1


    def occ_hndler_sheet_user(self):

        def generate_list(list, route):
            _list = []
            for item in list:
                _list.append(item)

            # Set route length
            if route == 'dermal':
                length = 6
            elif route == 'inhal':
                length = 4
            else:
                return None

            # Append list with 'None's to reach required length
            if len(_list) != length:
                if len(_list) > length:
                    return None
                else:
                    length_diff = length - len(_list)
                    i = 0
                    while i < length_diff:
                        _list.append(None)
                        i += 1

            return _list

        def generate_dermal_class_instances(attr_list):
            return ore_xls_formatter.OreXlsOccHndlerOutputsDermal(
                #  sl_no_g, sl_g, dl_g, sl_g_crh, dl_g_crh, ec
                attr_list[0],
                attr_list[1],
                attr_list[2],
                attr_list[3],
                attr_list[4],
                attr_list[5]
            )

        def generate_inhal_class_instances(attr_list):
            return ore_xls_formatter.OreXlsOccHndlerOutputsInhal(
                #  sl_no_g, sl_g, dl_g, sl_g_crh, dl_g_crh, ec
                attr_list[0],
                attr_list[1],
                attr_list[2],
                attr_list[3]
            )

        output = self.ore_obj.output

        count = 0
        for id, data in output.items():
            """
            Loop over each 'row' of output data from OreCalculator assigning the JSON data to their respective
            object attributes.  Each of these class instances will be used to write the data to the XLSX file.
            """

            # Dermal class instances
            dermal_unit_exp = generate_list(data['dermal_unit_exp'], 'dermal')
            dermal_exp = generate_list(data['dermal_exp'], 'dermal')
            dermal_dose = generate_list(data['dermal_dose'], 'dermal')
            dermal_moe = generate_list(data['dermal_moe'], 'dermal')
            occ_hndler_tab_output_dermal_unit_exp = generate_dermal_class_instances(dermal_unit_exp)
            occ_hndler_tab_output_dermal_exp = generate_dermal_class_instances(dermal_exp)
            occ_hndler_tab_output_dermal_dose = generate_dermal_class_instances(dermal_dose)
            occ_hndler_tab_output_dermal_moe = generate_dermal_class_instances(dermal_moe)

            # Inhalation class instances
            inhal_unit_exp = generate_list(data['inhal_unit_exp'], 'inhal')
            inhal_exp = generate_list(data['inhal_exp'], 'inhal')
            inhal_dose = generate_list(data['inhal_dose'], 'inhal')
            inhal_moe = generate_list(data['inhal_moe'], 'inhal')
            occ_hndler_tab_output_inhal_unit_exp = generate_inhal_class_instances(inhal_unit_exp)
            occ_hndler_tab_output_inhal_exp = generate_inhal_class_instances(inhal_exp)
            occ_hndler_tab_output_inhal_dose = generate_inhal_class_instances(inhal_dose)
            occ_hndler_tab_output_inhal_moe = generate_inhal_class_instances(inhal_moe)

            # Populate Columns A-I (inputs)
            occ_hndler_tab_input = ore_xls_formatter.OreXlsOccHndlerInputs(
                #  worker, formulation, app_equip, app_type, crop_target,
                #  app_rate, app_rate_unit, amount_handled, amount_handled_unit
                data['activity'],
                data['formulation'],
                data['app_equip'],
                data['app_type'],
                data['crop_target'],
                data['app_rate'],
                data['app_rate_unit'],
                data['area_treated'],
                data['area_treated_unit']
            )
            ordered_attrs = occ_hndler_tab_input.get_attrs()

            i = 0
            while i < len(ordered_attrs):
                self.ws_occ_handler.write(count + 2, i, ordered_attrs[i])
                i += 1

            # Populate Columns J-end (outputs)


            # Iterator counter for each set of output "rows"
            count += 1


class ToxExpoInputChemicalLabels(object):
    def __init__(self):
        self.chemical_info = 'CHEMICAL INFO'
        self.active_ingredient = 'Active ingredient:'
        self.exp_duration = 'Exposure Duration: \n(for multiple exposure durations, create new files)'


class ToxExpoInputToxicityLabels(object):
    def __init__(self):
        self.toxicity_header = 'Toxicity'
        self.dermal = 'Dermal'
        self.inhalation = 'Inhalation'
        self.non_cancer = 'Non-cancer'
        self.absorption = 'Absorption'
        self.pod = 'POD (mg/kg/day)'
        self.pod_source = 'POD source/study'
        self.loc = 'LOC'
        self.abs_fraction = 'Fraction (0-1)'
        self.abs_source = 'Absorption source/study'
        self.inhal_oral = ' - oral study'
        self.inhal_hec_83 = ' - from HEC (8.3 L/min'
        self.inhal_hec_167 = ' - from HEC (16.7 L/min'
        self.inhal_hec_29 = ' - from HEC (29 L/min'


class ToxExpoInputBodyWeightLabels(object):
    def __init__(self):
        self.bw_header = 'Body Weight (kg)'
        self.dermal = 'Dermal'
        self.inhalation = 'Inhalation'
        self.non_cancer = 'For non-cancer risks'
        self.adults = 'Adults'


class CropTargetLabels(object):
    def __init__(self):
        self.crop = 'Crop'
        self.tolerance_group = '40 CFR 180 (Tolerance Groups)'
        self.group = 'Group #'
        self.group_name = 'Group Name'
        self.sub_group = 'Sub-group #'
        self.sub_group_name = 'Sub-group Name'
        self.crop_target = 'Handler Crop/Target Category'


class OccHandlerNonCancerInputsLabels(object):
    def __init__(self):
        self.exp_scenario = 'Exposure Scenario'
        self.worker = 'Worker Activity'
        self.formulation = 'Formulation'
        self.app_equip = 'Application \nEquipment'
        self.app_type = 'Application Type'
        self.crop_target = 'Crop/Target Category'
        self.app_rate = 'Application Rate'
        self.app_rate_value = 'Value'
        self.app_rate_unit = 'Units'


class OccHandlerNonCancerOutputsLabels(object):
    def __init__(self):
        self.area_treated = 'Amount Handled / Area \nTreated'
        self.area_treated_value = 'Value'
        self.area_treated_unit = 'Units'
        # Dermal
        self.dermal_unit_exp = 'Dermal Unit Exposures (ug/lb ai)'
        self.dermal_exp = 'Dermal Exposure (mg/day)'
        self.dermal_dose = 'Dermal Dose (mg/kg/day)'
        self.dermal_moe = 'Dermal MOE'
        self.sl_no_g = 'SL/No G'
        self.sl_g = 'SL/G'
        self.dl_g = 'DL/G'
        self.sl_g_crh = 'SL/G/CRH'
        self.dl_g_crh = 'DL/G/CRH'
        self.ec = 'EC'
        # Inhalation
        self.inhal_unit_exp = 'Inhalation Unit Exposures (ug/lb ai)'
        self.inhal_exp = 'Inhalation Exposure (mg/day)'
        self.inhal_dose = 'Inhalation Dose (mg/kg/day)'
        self.inhal_moe = 'Inhalation MOE'
        self.no_r = 'No-R'
        self.pf5_r = 'PF5 R'
        self.pf10_r = 'PF10 R'

    def get_dermal_ppe_labels(self):
        return [ self.sl_no_g, self.sl_g, self.dl_g, self.sl_g_crh, self.dl_g_crh, self.ec ]

    def get_inhal_ppe_labels(self):
        return [ self.no_r, self.pf5_r, self.pf10_r, self.ec ]


def create_temp_dir():
    """
    Builds the absolute path to temporary Excel spreadsheet using a random string generator to create a subdirectory
    :return: String
    """
    # Generate a random ID for file save
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def create_temp_path(temp_dir_name):
        return os.path.join(os.environ['PROJECT_PATH'], 'models', 'ore', 'static', 'ore', temp_dir_name)

    temp_dir_name = id_generator()
    temp_path = create_temp_path(temp_dir_name)
    try:  # try to create temp dir
        os.mkdir(temp_path)
    except OSError, os_e:
        shutil.rmtree(temp_path)
        try:  # try again!! this time with the temp_path removed
            os.mkdir(temp_path)
        except OSError, os_e2:  # if this fails log it and return None
            logging.exception(os_e2)
            return None

    return temp_path, temp_dir_name


def generate_xlsx(json):
    """
    Main entry-point method for creating Excel spreadsheet from OreCalculator JSON.
    :param json:
    :return: string
    """

    # TODO: This method currently writes XLSX to disk, and serves that as static file to user
    # TODO: Preferred approach is to create XLSX in memory (StringIO) and serve that back to user
    # TODO: Issue with StringIO approach is the AJAX POSTing of JSON does not allow for file to be returned...
    # TODO: ...The JSON is complicated and cumbersome to convert to FormObject which allows for file download to user.
    # TODO: Currently, this method returns relative path to XLSX, and that is submitted as Form in 'ore_scripts.js' to download the file to the user.

    try:
        # Allocate memory space for workbook to be created
        # output = StringIO.StringIO()

        temp_path_name = create_temp_dir()
        output_file = os.path.join(temp_path_name[0], 'ore.xlsx')

        if output_file is not None:
            # Format JSON for OreXls
            ore_obj = ore_xls_formatter.OreOutputFormatter(json)

            # Create spreadsheet instance
            ore_xlsx = OreXls(output_file, ore_obj)

            # Generate the content for each worksheet
            ore_xlsx.tox_expo_inputs_sheet()
            ore_xlsx.crop_target_sheet()
            ore_xlsx.occ_handler_sheet_inputs()
            ore_xlsx.tox_expo_sheet_user()
            ore_xlsx.crop_target_sheet_user()
            ore_xlsx.occ_hndler_sheet_user()

            # Close the Excel workbook file
            ore_xlsx.close()

        else:
            return None

    except:
        return None

    return temp_path_name[1]