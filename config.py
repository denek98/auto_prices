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
            'Количество 0 дней': [],
            'Количество 1 дней': [5],
            'Количество 2 дней': [],
            'Название': 3,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Фордс
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Техномир
# ----------------------------------------------------------------------------------------------------
    'tehnomir': {
        'supplier_folder': 'Техномир',
        'output_filename': 'tehnomir.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 1,
            'Артикул': 2,
            'Цена': 5,
            'Количество 1 дней': [4],
            'Количество 2 дней': [4],
            'Количество 3 дней': [4],
            'Название': 3,
            'Множитель цены': 1,
            'Колонка с курсом валюты': 10
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Техномир
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Центр Газ
# ----------------------------------------------------------------------------------------------------
    'centr_gaz': {
        'supplier_folder': 'Центр Газ',
        'output_filename': 'centr_gaz.csv',
        'Количество бесполезных строк': 1,
        'supplier_columns_dict': {
            'Производитель': 5,
            'Артикул': 6,
            'Цена': 3,
            'Количество 0 дней': [],
            'Количество 1 дней': [9],
            'Количество 2 дней': [],
            'Название': 1,
            'Множитель цены': 28.3
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Центр Газ
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# Начало Елит
# ----------------------------------------------------------------------------------------------------
    'elit': {
        'supplier_folder': 'Елит',
        'output_filename': 'elit.csv',
        'Количество бесполезных строк': 2,
        'supplier_columns_dict': {
            'Производитель': 3,
            'Артикул': 2,
            'Цена': 6,
            'Количество 0 дней': [7, 8],
            'Количество 1 дней': [9, 10, 11],
            'Количество 2 дней': [12],
            'Название': 4,
            'Множитель цены': 1
        }
    },
# ----------------------------------------------------------------------------------------------------
# Конец Секции Елит
# ----------------------------------------------------------------------------------------------------
}
