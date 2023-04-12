import csv
import os
import re
from app.lib.utils import extract_digits

default_args = {
    'String': 255,
    'DateTime': ['timezone=True', 'default=datetime.utcnow, onupdate=datetime.utcnow'],
    'Date': None
}


def is_float(item):
    if isinstance(item, float):
         return True

    pattern = '^[0-9.]+$'
    item = re.findall(pattern, item)

    return True if item else False


def is_int(item):
    if isinstance(item, int):
         return True

    pattern = '^[0-9]+$'
    item = re.findall(pattern, item)

    return True if item else False


def is_date(item):
    if '/' in item:
        item = item.split('/')
    elif '-' in item:
        item = item.split('-')

    if not isinstance(item, list):
        return False

    if len(item) == 3:
        return True

    try:
        item = list(map(int, item))
    except ValueError as ex:
        return False

    return True


def is_datetime(item):
    date_split = []
    if '/' in item:
        date_split = item.split('/')
    elif '-' in item:
        date_split = item.split('-')

    if len(date_split) == 3 and ':' in item and len(item.split(':')) == 3:
        return True

    return False


def get_data_type(items):
    items = list((filter(lambda item: item, items)))
    if not items:
        return 'String'

    item = items[-1]
    if not item:
        return 'String'

    if is_int(item):
        return 'Integer'

    elif is_float(item):
        return 'Float'

    elif is_date(item):
        return 'Date'
    
    elif is_datetime(item):
        return 'DateTime'

    else:
        return 'String'


def get_column_data_types(csv_file):
    rows = csv.DictReader(csv_file, delimiter='|')
    headers = None
    data = {}
    data_types = {}
    for row in rows:
        if not headers:
            headers = list(row.keys())

        for header in headers:
            item = row[header]
            items = data.get(header, [])
            items.append(item)
            data[header] = items

    for header, items in data.items():
        data_type = get_data_type(items)
        data_types[header] = data_type

    return data_types


def format_col_name(col_name):
    col_name = col_name.replace('(', '')
    col_name = col_name.replace(')', '')
    col_name = col_name.replace('-', '_')
    col_name = col_name.replace(':', '')
    col_name = col_name.replace('$', '_dollar_')
    col_name = col_name.replace('&', '_and_')
    col_name = col_name.replace('%', '_perc_')
    col_name = col_name.replace('>', '_gt_')
    col_name = col_name.replace('<', '_lt_')
    col_name = col_name.replace('/', '_by_')
    col_name = col_name.replace('+', '')
    col_name = col_name.replace('#', '')
    col_name = col_name.replace('____', '_')
    col_name = col_name.replace('___', '_')
    col_name = col_name.replace('__', '_')
    col_name = col_name.strip().split()
    col_name = [part.lower() for part in col_name]

    col_name = '_'.join(col_name)
    col_name = col_name.replace('____', '_')
    col_name = col_name.replace('___', '_')
    col_name = col_name.replace('__', '_')

    if col_name[0].isdigit():
        digits = extract_digits(col_name)
        col_name = col_name.split('_')
        print('******', col_name)
        col_name = [col_name[1]] + [digits] + col_name[2:]
        col_name = '_'.join(col_name)

    return col_name


def write_database_model(model_file, table_name, schema_name, columns):

    imports = '''
from sqlalchemy import Column
from sqlalchemy import String, Date, Float, Integer

from app.models.base_model import BaseModel, UpdateMixin

'''

    class_name = ''.join([part.capitalize() for part in table_name.split('_')])
    schema = {'schema': schema_name}

    model_class = f'''
class {class_name}(BaseModel, UpdateMixin):
    __tablename__ = '{table_name}'
    __table_args__ = (
        {schema},
    )

'''

    model_file.write(imports)
    model_file.write(model_class)

    for column_name, column_type in columns.items():
        try:
            args = default_args[column_type]
        except KeyError:
            rhs = f'Column({column_type}())'
        else:
            if isinstance(args, list):
                rhs = f'Column({column_type}({args[0]}), {args[1]})'
            else:
                if args:
                    rhs = f'Column({column_type}({args}))'
                else:
                    rhs = f'Column({column_type}())'

        col_name = format_col_name(column_name)
        model_file.write(f'\t{col_name} = {rhs}\n')


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model_path = os.path.join(dir_path, '..', 'app', 'models', 'gs_data')

    table_names = [f'sheet{i}' for i in range(1, 15)]

    # Generate Models
    for table_name in table_names:
        with open(os.path.join(dir_path, f'{table_name}.csv'), 'r') as csv_file:
            columns = get_column_data_types(csv_file)
            for column_name, column_type in columns.items():
                print(column_name, column_type)
            print(table_name)

        with open(os.path.join(model_path, f'{table_name}.py'), 'w') as model_file:
            write_database_model(model_file, table_name, 'gs_data', columns)

    # Get Headers
    # with open('cols.csv', 'r') as cols:
    #     with open('cols_format.csv', 'w') as cols_format:
    #         for line in cols:
    #             column_names = []
    #             line = line.strip().split('|')
    #             for col_name in line:
    #                 col_name = format_col_name(col_name)
    #                 column_names.append(col_name)

                # cols_format.write(f'{"|".join(column_names)}\n')
