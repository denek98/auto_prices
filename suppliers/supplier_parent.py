import config
import os
import shutil
from zipfile import ZipFile
import pandas as pd
from multiprocessing import Pool
import math
import re

class SupplierParent:
    def __init__(self):
        os.makedirs(config.input_folder_name, exist_ok=True)
        os.makedirs(config.output_folder_name, exist_ok=True)
        self._resulted_df = pd.DataFrame()
        self._primary_columns_from_excel_list = [key for key in config.final_columns_names_dict.keys() if key not in ['Срок поставки','Количество']]
        self._delivery_days_options_list = [0,1,2]

    def _repack_excel_from_1c(self):
        try:
            tmp_folder = '/tmp/convert_wrong_excel/'
            os.makedirs(tmp_folder, exist_ok=True)
            with ZipFile(self._input_excel_path) as excel_container:
                excel_container.extractall(tmp_folder)
            wrong_file_path = os.path.join(tmp_folder, 'xl', 'SharedStrings.xml')
            correct_file_path = os.path.join(tmp_folder, 'xl', 'sharedStrings.xml')
            os.rename(wrong_file_path, correct_file_path) 
            shutil.make_archive('yourfile', 'zip', tmp_folder)
            os.rename('yourfile.zip', self._input_excel_path)
        except:
            return False
        return True

    def _get_excel_file_path(self):
        supplier_input_folder_path = os.path.join(config.input_folder_name, self._supplier_dict['supplier_folder'])
        supplier_excel_file_list = os.listdir(supplier_input_folder_path)
        supplier_excel_file = [file for file in supplier_excel_file_list if any(['xl' in file,'csv' in file])][0]
        input_excel_path = os.path.join(supplier_input_folder_path, supplier_excel_file)
        return input_excel_path

    def _df_to_cannonical(self):
        self._resulted_df = self._resulted_df[config.final_columns_names_dict.keys()]
        self._resulted_df['Цена'] = self._resulted_df['Цена'].apply(self._normalize_price)
        for column in config.final_columns_names_dict.keys():
            self._resulted_df[column] = self._resulted_df[column].astype(config.final_columns_names_dict[column])
        self._resulted_df.drop_duplicates(subset=['Артикул','Срок поставки'],inplace=True)
        self._drop_useless_rows()
        self._apply_discount_for_brand()
        return True

    def run(self):
        self._read_df.dropna(subset=[self._columns_dict['Артикул']-1,self._columns_dict["Цена"]-1,self._columns_dict["Производитель"]-1],inplace=True)
        with Pool(3) as pool:
            df_list = pool.map(self._create_dataframe_for_delivery_days,self._delivery_days_options_list)
        self._resulted_df = pd.concat(df_list)
        self._df_to_cannonical()
        self._resulted_df.to_csv(self._output_csv_path,index=False,header=None,sep=';')
        return True
        
    def _count_quantity_for_n_days(self,series,delivery_days):
        if self._columns_dict[f'Количество {delivery_days} дней']:
            quantity = 0
            for column_index in self._columns_dict[f'Количество {delivery_days} дней']:
                if str(series.iloc[column_index - 1]) != 'nan':
                    quantity += self._convert_quantity_to_int(series.iloc[column_index - 1])
            return quantity

    def _apply_discount_for_brand(self):
        if 'Наценка на производителей' in self._columns_dict.keys():
            self._resulted_df['Цена'] = self._resulted_df.apply(self._count_discount,axis=1)
        return True

    def _count_discount(self,series):
        lower_brands = [brand.lower() for brand in self._columns_dict['Наценка на производителей'].keys()]
        if series['Производитель'].lower() in lower_brands:
            series['Цена'] *=  self._columns_dict['Наценка на производителей'][series['Производитель']]
        return series['Цена']


    @staticmethod
    def _convert_quantity_to_int(quantity):
        bad_symbols = '+-><? '
        try:
            quantity = str(quantity)
            for symbol in bad_symbols:
                quantity = quantity.replace(symbol,'')
            quantity = quantity.replace(',','.')
            quantity = quantity.strip()
            quantity = float(quantity)
            quantity = math.ceil(quantity)
            return int(quantity)
        except:
            return 0

    def _normalize_price(self,price):
        price = str(price).replace(',','.').replace(' ','').strip()
        return float(price) * self._columns_dict['Множитель цены']
        

    @staticmethod
    def _check_for_cirrilyc(supplier):
        return bool(re.search('[а-яА-Я]', supplier))


    def _drop_useless_rows(self):
        self._resulted_df.drop(self._resulted_df[self._resulted_df['Производитель'] == ''].index, inplace=True)
        self._resulted_df.drop(self._resulted_df[self._resulted_df['Артикул'] == ''].index, inplace=True)
        self._resulted_df.drop(self._resulted_df[self._resulted_df['Производитель'] == 'nan'].index, inplace=True)
        self._resulted_df.drop(self._resulted_df[self._resulted_df['Артикул'] == 'nan'].index, inplace=True)
        self._resulted_df.drop(self._resulted_df[self._resulted_df['Цена'].astype(int) == 0].index, inplace=True)
        self._resulted_df.drop(self._resulted_df[self._resulted_df['Количество'] == 0].index, inplace=True)
        self._resulted_df.drop(self._resulted_df[self._resulted_df['Производитель'].map(self._check_for_cirrilyc) == True].index, inplace=True)
        return True
        

