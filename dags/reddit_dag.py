from airflow import DAG
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # get absolute file, get dir name (dags), first -- get the name of DAG(Reddit...)

default_args = {
    'owner': 'kate',
    'start_date': datetime(2024, 03, 11)
}

file_postfix = datetime.now().strftime((""))