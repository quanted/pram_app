__author__ = 'jflaisha'


class OreOutputFormatter(object):
    def __init__(self, json):
        self.json = json
        self.json_checker()

    def json_checker(self):

        try:
            self.input = self.json['input']
        except KeyError:
            raise KeyError('JSON object is missing "input" key')

        try:
            self.output = self.json['output']
        except KeyError:
            raise KeyError('JSON object is missing "output" key')


class OreXlsToxExpo(object):
    def __init__(self, active_ingredient, exposure_duration,
                 dermal_nc_pod, dermal_nc_pod_source, dermal_nc_loc, dermal_abs_fraction, dermal_abs_source,
                 inhal_nc_pod_oral, inhal_nc_pod_hec83, inhal_nc_pod_hec167, inhal_nc_pod_hec29, inhal_nc_source,
                 inhal_nc_loc, inhal_abs_fraction, inhal_abs_source, bw_dermal, bw_inhal):

        self.active_ingredient = active_ingredient
        self.exposure_duration = exposure_duration
        self.dermal_nc_pod = dermal_nc_pod
        self.dermal_nc_pod_source = dermal_nc_pod_source
        self.dermal_nc_loc = dermal_nc_loc
        self.dermal_abs_fraction = dermal_abs_fraction
        self.dermal_abs_source = dermal_abs_source
        self.inhal_nc_pod_oral = inhal_nc_pod_oral
        self.inhal_nc_pod_hec83 = inhal_nc_pod_hec83
        self.inhal_nc_pod_hec167 = inhal_nc_pod_hec167
        self.inhal_nc_pod_hec29 = inhal_nc_pod_hec29
        self.inhal_nc_source = inhal_nc_source
        self.inhal_nc_loc = inhal_nc_loc
        self.inhal_abs_fraction = inhal_abs_fraction
        self.inhal_abs_source = inhal_abs_source
        self.bw_dermal = bw_dermal
        self.bw_inhal = bw_inhal

    def get_attrs(self):
        """
        Get attributes of class in order of appearance in Excel spreadsheet
        """
        return ( self.active_ingredient, self.exposure_duration, self.dermal_nc_pod, self.dermal_nc_pod_source,
                 self.dermal_nc_loc, self.dermal_abs_fraction, self.dermal_abs_source, self.inhal_nc_pod_oral,
                 self.inhal_nc_pod_hec83, self.inhal_nc_pod_hec167, self.inhal_nc_pod_hec29, self.inhal_nc_source,
                 self.inhal_nc_loc, self.inhal_abs_fraction, self.inhal_abs_source, self.bw_dermal, self.bw_inhal )


class OreXlsCropTarget(object):
    def __init__(self, crop, group_no, group_name, subgroup_no, subgroup_name, crop_target):

        self.crop = crop
        self.group_no = group_no
        self.group_name = group_name
        self.subgroup_no = subgroup_no
        self.subgroup_name = subgroup_name
        self.crop_target = crop_target

    def get_attrs(self):
        """
        Get attributes of class in order of appearance in Excel spreadsheet
        """
        return ( self.crop, self.group_no, self.group_name, self.subgroup_no, self.subgroup_name, self.crop_target )

class OreXlsOccHndlerInputs(object):
    def __init__(self, worker, formulation, app_equip, app_type, crop_target,
                 app_rate, app_rate_unit, amount_handled, amount_handled_unit):

        self.worker = worker
        self.formulation = formulation
        self.app_equip = app_equip
        self.app_type = app_type
        self.crop_target = crop_target
        self.app_rate = app_rate
        self.app_rate_unit = app_rate_unit
        self.amount_handled = amount_handled
        self.amount_handled_unit = amount_handled_unit

    def get_attrs(self):
        """
        Get attributes of class in order of appearance in Excel spreadsheet
        """
        return ( self.worker, self.formulation, self.app_equip, self.app_type, self.crop_target,
                 self.app_rate, self.app_rate_unit, self.amount_handled, self.amount_handled_unit )


class OreXlsOccHndlerOutputsDermal(object):
    """
    Use for Dermal Unit Exposures, Dermal Exposures, Dermal Dose, and Dermal MOE
    """
    def __init__(self, sl_no_g, sl_g, dl_g, sl_g_crh, dl_g_crh, ec):

        self.sl_no_g = sl_no_g
        self.sl_g = sl_g
        self.dl_g = dl_g
        self.sl_g_crh = sl_g_crh
        self.dl_g_crh = dl_g_crh
        self.ec = ec

    def get_attrs(self):
        """
        Get attributes of class in order of appearance in Excel spreadsheet
        """
        return ( self.sl_no_g, self.sl_g, self.dl_g, self.sl_g_crh, self.dl_g_crh, self.ec )


class OreXlsOccHndlerOutputsInhal(object):
    """
    Use for Inhalation Unit Exposures, Inhalation Exposures, Inhalation Dose, and Inhalation MOE
    """
    def __init__(self, no_r, pf5_r, pf10_r, ec):

        self.no_r = no_r
        self.pf5_r = pf5_r
        self.pf10_r = pf10_r
        self.ec = ec

    def get_attrs(self):
        """
        Get attributes of class in order of appearance in Excel spreadsheet
        """
        return ( self.no_r, self.pf5_r, self.pf10_r, self.ec )