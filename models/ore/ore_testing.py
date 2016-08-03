import xlsxwriter

class OreXls(object):
    def __init__(self, xlsx, ore_obj):
        # self.wb = xlsxwriter.Workbook(xlsx, {'in_memory': True})  # Create Workbook in-memory
        self.wb = xlsxwriter.Workbook(xlsx)
        self.ws_tox_expo = self.wb.add_worksheet('TOX and EXPO INPUTS')
        self.ws_crop_target = self.wb.add_worksheet('Crop-Target Category Lookup')
        self.ws_occ_handler = self.wb.add_worksheet('OccHndler_Non-cancer')

    def close(self):
        self.wb.close()

xlsx = OreXls('temp.xlsx', None)
xlsx.close()