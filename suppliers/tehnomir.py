import pandas as pd 
import config
import os
from suppliers.supplier_parent import SupplierParent
from config import suppliers_dict
from multiprocessing import Pool


class Tehnomir(SupplierParent):
    def __init__(self):
        SupplierParent.__init__(self)
        self._supplier_name = 'tehnomir'
        self._supplier_dict = suppliers_dict[self._supplier_name]
        self._input_excel_path_list = self._get_excel_file_path_list()
        self._output_csv_path = os.path.join(config.output_folder_name, self._supplier_dict['output_filename'])
        self._columns_dict = self._supplier_dict['supplier_columns_dict']
        self._useless_rows_number = self._supplier_dict['Количество бесполезных строк']
        # self._read_df = self._read_from_excel()

    def _read_from_excel(self, file_path):
        read_df = pd.read_excel(file_path, skiprows=self._useless_rows_number, header=None)
        return read_df
        
    def _create_dataframe_for_delivery_days(self, file_path):
        delivery_days = file_path.split('.')[-2][-1]
        df_from_file = self._read_from_excel(file_path)
        df_for_delivery_days = pd.DataFrame()
        for key in self._columns_dict:
            if key in self._primary_columns_from_excel_list:
                df_for_delivery_days[key] = (df_from_file.iloc[:, self._columns_dict[key] - 1])
        df_for_delivery_days['Цена'] = df_from_file.iloc[:, self._columns_dict['Цена'] - 1].astype(float) * df_from_file.iloc[:, self._columns_dict['Колонка с курсом валюты'] - 1].astype(float)
        df_for_delivery_days['Количество'] = df_from_file.apply(self._count_quantity_for_n_days, args=(delivery_days,), axis=1)
        df_for_delivery_days = df_for_delivery_days[df_for_delivery_days['Количество'].notna()]
        df_for_delivery_days = df_for_delivery_days[df_for_delivery_days['Количество'] != 0]
        df_for_delivery_days['Срок поставки'] = delivery_days
        return df_for_delivery_days

    def _get_excel_file_path_list(self):
        supplier_input_folder_path = os.path.join(config.input_folder_name, self._supplier_dict['supplier_folder'])
        supplier_excel_file_list = os.listdir(supplier_input_folder_path)
        supplier_excel_file_names_list = [file for file in supplier_excel_file_list if any(['xl' in file, 'csv' in file]) and '~$' not in file]
        input_excel_files_path_list = [os.path.join(supplier_input_folder_path, item) for item in supplier_excel_file_names_list]
        return input_excel_files_path_list

    def run(self):
        # self._read_df.dropna(subset=[self._columns_dict['Артикул']-1,self._columns_dict["Цена"]-1,self._columns_dict["Производитель"]-1],inplace=True)
        # with Pool(3) as pool:
        #     df_list = pool.map(self._create_dataframe_for_delivery_days, self._input_excel_path_list)
        df_list = [self._create_dataframe_for_delivery_days(input_excel) for input_excel in self._input_excel_path_list]
        self._resulted_df = pd.concat(df_list)
        self._df_to_cannonical()
        self._resulted_df.to_csv(self._output_csv_path, index=False, header=None, sep=';')
        return True


