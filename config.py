final_columns_names_dict = {'Производитель':'str','Артикул':'str','Цена':'float','Количество':'int','Срок поставки':'int','Название':'str'}
input_folder_name = 'Входящие прайсы'
output_folder_name = 'Результат прайсы'

# Количество, артикул, произовдитель, цена - primary keys (в т.ч. нули)
# Исключаем кириллицу в артикуле и производителе

suppliers_dict = {

# ----------------------------------------------------------------------------------------------------
# Начало Секции АвтоНова
# ----------------------------------------------------------------------------------------------------
    'avtonova' : {
        'supplier_folder' : 'АвтоНова',
        'output_filename' : 'avtonova.csv',
        'Количество бесполезных строк' : 2,
        'supplier_columns_dict' : {
            'Производитель': 4,
            'Артикул': 3,
            'Цена': 14,
            'Количество 0 дней': [11],
            'Количество 1 дней': [6],
            'Количество 2 дней': [7,8,9,10,12,13],
            'Название': 5,
            'Множитель цены' : 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции АвтоНова
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------
# Начало Секции ИнтерКарс
# ----------------------------------------------------------------------------------------------------
# Цена умножается на 1.2
# Плюсы в наличии убираются
# ----------------------------------------------------------------------------------------------------
    'intercars' : {
        'supplier_folder' : 'ИнтерКарс',
        'output_filename' : 'intercars.csv',
        'Количество бесполезных строк' : 1,
        'supplier_columns_dict' : {
            'Производитель': 5,
            'Артикул': 3,
            'Цена': 6,
            'Количество 0 дней': [7],
            'Количество 1 дней': [8],
            'Количество 2 дней': [9],
            'Название': 4,
            'Множитель цены' : 1.2
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции ИнтерКарс
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------
# Начало Секции КиаПартс
# ----------------------------------------------------------------------------------------------------
# Наличие есть = 3
# Днепр = 0 дней, не днепр = 1
# Количество везде 3 (7 столбец)
# Приходится переоткрывать вручную
# ----------------------------------------------------------------------------------------------------
    'kiaparts' : {
        'supplier_folder' : 'КиаПартс',
        'output_filename' : 'kiaparts.csv',
        'Количество бесполезных строк' : 2,
        'supplier_columns_dict' : {
            'Производитель': 5,
            'Артикул': 1,
            'Цена': 6,
            'Количество 0 дней': [8],
            'Количество 1 дней': [8],
            'Название': 3,
            'Множитель цены' : 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции КиаПартс
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------
# Начало Секции МастерСервис
# ----------------------------------------------------------------------------------------------------
# Группировка, соединенные ячейки?
# Если убрать обьединение то нужно выкинуть пустой артикул
# Если производитель содержит MSG - наценка 10%
# Производителя нужно задавать четко
# ----------------------------------------------------------------------------------------------------
    'masterservis' : {
        'supplier_folder' : 'МастерСервис',
        'output_filename' : 'masterservice.csv',
        'Количество бесполезных строк' : 8,
        'supplier_columns_dict' : {
            'Производитель': 1,
            'Артикул': 3,
            'Цена': 6,
            'Количество 0 дней': [7],
            'Количество 1 дней': [8,9,10,13],
            'Количество 2 дней': [11,12],
            'Название': 5,
            'Множитель цены' : 1,
            'Наценка на производителей' : {
                'MSG': 1.1,
            }
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции МастерСервис
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------
# Начало Секции Владислав
# ----------------------------------------------------------------------------------------------------
# Ориентируемся на остатки по складам (Днепр и не Днепр)
# Убираем галочку больше в остатках
# Нули в остатках можем выкинуть
# ----------------------------------------------------------------------------------------------------
    'vladislav' : {
        'supplier_folder': 'Владислав',
        'output_filename': 'vladislav.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 2,
            'Артикул': 4,
            'Цена': 5,
            'Количество 0 дней': [6],
            'Количество 1 дней': [7],
            'Количество 2 дней': [],
            'Название': 8,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Владислав
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Секции Весна
# ----------------------------------------------------------------------------------------------------
    'vesna': {
        'supplier_folder': 'Весна',
        'output_filename': 'vesna.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 3,
            'Артикул': 2,
            'Цена': 10,
            'Количество 0 дней': [7],
            'Количество 1 дней': [8],
            'Количество 2 дней': [9],
            'Название': 4,
            'Множитель цены': 32.46
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Весна
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Секции Юникс
# ----------------------------------------------------------------------------------------------------
    'uniks': {
        'supplier_folder': 'Юникс',
        'output_filename': 'uniks.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 3,
            'Артикул': 1,
            'Цена': 5,
            'Количество 0 дней': [13],
            'Количество 1 дней': [6, 8, 9, 10],
            'Количество 2 дней': [7, 11, 12],
            'Название': 2,
            'Множитель цены': 1,
            'Наценка на производителей': {
                'SATO TECH': 1.14,
            }
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Юникс
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Фордс
# ----------------------------------------------------------------------------------------------------
    'fords': {
        'supplier_folder': 'Фордс',
        'output_filename': 'fords.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 6,
            'Артикул': 1,
            'Цена': 4,
            'Количество 0 дней': [5],
            'Количество 1 дней': [],
            'Количество 2 дней': [],
            'Название': 3,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Фордс
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Скар
# ----------------------------------------------------------------------------------------------------
    'scar': {
        'supplier_folder': 'Скар',
        'output_filename': 'scar.csv',
        'Количество бесполезных строк': 17,
        'supplier_columns_dict': {
            'Производитель': 3,
            'Артикул': 2,
            'Цена': 5,
            'Количество 0 дней': [7],
            'Количество 1 дней': [8,9],
            'Количество 2 дней': [],
            'Название': 4,
            'Множитель цены': 0.7
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Скар
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Омега
# ----------------------------------------------------------------------------------------------------
    'omega': {
        'supplier_folder': 'Омега',
        'output_filename': 'omega.csv',
        'Количество бесполезных строк': 1,
        'Номер вкладки с полезной информацией' : 2,
        'supplier_columns_dict': {
            'Производитель': 1,
            'Артикул': 3,
            'Цена': 7,
            'Количество 0 дней': [14],
            'Количество 1 дней': [11],
            'Количество 2 дней': [13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35],
            'Название': 4,
            'Множитель цены': 1,
            'Наценка на производителей': {
                'SANGSIN': 0.97,
                'CTR': 0.97,
            },
        },
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Омега
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало СоллиПлюс
# ----------------------------------------------------------------------------------------------------
    'solly_plus': {
        'supplier_folder': 'СоллиПлюс',
        'output_filename': 'solly_plus.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 1,
            'Артикул': 2,
            'Цена': 5,
            'Количество 0 дней': [],
            'Количество 1 дней': [4],
            'Количество 2 дней': [],
            'Название': 3,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции СоллиПлюс
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало МаксПартс
# ----------------------------------------------------------------------------------------------------
    'max_parts': {
        'supplier_folder': 'МаксПартс',
        'output_filename': 'max_parts.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 3,
            'Артикул': 1,
            'Цена': 5,
            'Количество 0 дней': [],
            'Количество 1 дней': [6],
            'Количество 2 дней': [],
            'Название': 4,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции МаксПартс
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Зенит
# ----------------------------------------------------------------------------------------------------
    'zenit': {
        'supplier_folder': 'Зенит',
        'output_filename': 'zenit.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 4,
            'Артикул': 3,
            'Цена': 10,
            'Количество 0 дней': [6],
            'Количество 1 дней': [5,8],
            'Количество 2 дней': [7],
            'Название': 2,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Зенит
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Елит ОЕМ
# ----------------------------------------------------------------------------------------------------
    'elit_oem': {
        'supplier_folder': 'ЕлитОем',
        'output_filename': 'elit_oem.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 3,
            'Артикул': 2,
            'Цена': 6,
            'Количество 0 дней': [],
            'Количество 1 дней': [],
            'Количество 2 дней': [9],
            'Название': 4,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Елит ОЕМ
# ----------------------------------------------------------------------------------------------------
}
