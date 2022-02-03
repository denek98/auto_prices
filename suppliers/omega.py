import pandas as pd 
import config
import os
from suppliers.supplier_parent import SupplierParent
from config import suppliers_dict


class Omega(SupplierParent):
    def __init__(self):
        SupplierParent.__init__(self)
        self._supplier_name = 'omega'
        self.set_logger('omega')
        self._supplier_dict = suppliers_dict[self._supplier_name]
        self._input_excel_path = self._get_excel_file_path()
        self._output_csv_path = os.path.join(config.output_folder_name, self._supplier_dict['output_filename'])
        self._columns_dict = self._supplier_dict['supplier_columns_dict']
        self._useless_rows_number = self._supplier_dict['Количество бесполезных строк']
        self._read_df = pd.DataFrame()

    def _read_from_excel(self):
        self._repack_excel_from_1c()
        read_df = pd.read_excel(self._input_excel_path, skiprows=self._useless_rows_number, header=None, sheet_name=self._supplier_dict['Номер вкладки с полезной информацией'] - 1)
        return read_df





