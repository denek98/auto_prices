import pandas as pd 
import config
import os
from suppliers.supplier_parent import SupplierParent
from config import suppliers_dict
from loguru import logger


class KiaParts(SupplierParent):
    def __init__(self):
        SupplierParent.__init__(self)
        self._supplier_name = 'kiaparts'
        self.set_logger('kiaparts')
        self._supplier_dict = suppliers_dict[self._supplier_name]
        self._input_excel_path = self._get_excel_file_path()
        self._output_csv_path = os.path.join(config.output_folder_name, self._supplier_dict['output_filename'])
        self._columns_dict = self._supplier_dict['supplier_columns_dict']
        self._useless_rows_number = self._supplier_dict['Количество бесполезных строк']
        self._read_df = pd.DataFrame()

    def _read_from_excel(self):
        read_df = pd.read_excel(self._input_excel_path, skiprows=self._useless_rows_number, engine='xlrd', header=None)
        return read_df

    def _create_dataframe_for_delivery_days(self, delivery_days):
        df_for_delivery_days = pd.DataFrame()
        for key in self._columns_dict:
            if key in self._primary_columns_from_excel_list:
                df_for_delivery_days[key] = (self._read_df.iloc[:, self._columns_dict[key] - 1])
        df_for_delivery_days['Количество'] = self._read_df.apply(self._count_quantity_for_n_days, args=(delivery_days,), axis=1)
        df_for_delivery_days = df_for_delivery_days[df_for_delivery_days['Количество'].notna()]
        df_for_delivery_days = df_for_delivery_days[df_for_delivery_days['Количество'] != 0]
        df_for_delivery_days['Срок поставки'] = delivery_days
        df_for_delivery_days = df_for_delivery_days.groupby(by=(self._primary_columns_from_excel_list + ['Срок поставки'])).sum().reset_index()
        return df_for_delivery_days

    def run(self):
        logger.info(f'Старт обработки поставщика {self._supplier_name}')
        try:
            self._read_df = self._read_from_excel()
            df_list = [self._create_dataframe_for_delivery_days(day) for day in [0, 1]]
            self._resulted_df = pd.concat(df_list)
            self._df_to_cannonical()
            self._resulted_df.to_csv(self._output_csv_path, index=False, header=None, sep=';')
            return True
        except Exception as e:
            logger.error(f'Ошибка при обработке {self._supplier_name}. Ошибка: {e}')
            return False

    def _count_quantity_for_n_days(self, series, delivery_days):
        if self._columns_dict[f'Количество {delivery_days} дней']:
            quantity = 0
            if delivery_days == 0:
                for column_index in self._columns_dict[f'Количество {delivery_days} дней']:
                    if 'Днепр' in series.iloc[column_index - 1]:
                        quantity += 3
            else:
                for column_index in self._columns_dict[f'Количество {delivery_days} дней']:
                    if not 'Днепр' in series.iloc[column_index - 1]:
                        quantity += 3
        return quantity


