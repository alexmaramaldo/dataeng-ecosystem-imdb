import os

from airflow import DAG

from utils.utils_common_vars import datetime, URLS_IMDB
from operators.imdb_download_from_source_operator import ImdbDownloadFromSourceOperator


# Percorre todos os modulos e cria as dags dinamicamente
for module in URLS_IMDB:
    with DAG(
            dag_id=f"download_{module}_dag",
            start_date=datetime(2021,1,1),
            schedule_interval=None,
            catchup=False) as dag:

       download_task = ImdbDownloadFromSourceOperator(
          task_id=f"download_{module}_task", url=URLS_IMDB[module]
       )
       # TASKS
       download_task
