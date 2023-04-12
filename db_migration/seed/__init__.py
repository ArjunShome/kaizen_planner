"""
This is an independent script which creates the schema and tables in the database.
"""

import csv
import os
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import KaizenQuestion, KaizenAnalysisQuestion

table_sheet_map = {
    'kaizen_question': KaizenQuestion, 'kaizen_analysis_question': KaizenAnalysisQuestion
}

endpoint = 'postgresql://postgres:postgres@localhost:5432/kaizen_planner'
base_dir = 'home/arjun/Partial_life/Work/Internal_Work/kaizen_planner'

engine = create_engine(endpoint, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


def set_attributes(obj, values):
    for key, value in values.items():
        if hasattr(obj, key) and value:
            value = value.strip()
            if '/' in value:
                try:
                    value = datetime.strptime(value, '%d/%m/%Y').date()
                except Exception as ex:
                    value = value
            setattr(obj, key, value)
    return obj


for sheet_name, ModelClass in table_sheet_map.items():
    # print(os.path.join('db_migration','seed',f'{sheet_name}.csv'), ModelClass)
    with open(os.path.join('db_migration','seed',f'{sheet_name}.csv'), 'r') as sheet:
        rows = csv.DictReader(sheet, delimiter=',')
        print(f'Loading {sheet_name}')
        for row in rows:
            obj = ModelClass()
            obj = set_attributes(obj, row)
            session.add(obj)
            session.commit()
