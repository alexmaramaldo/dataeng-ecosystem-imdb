from airflow import DAG
from datetime import datetime
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

from operators.imdb_ingest_to_parquet_operator import IMDBIngestToParquetOperator

from utils.utils_common_vars import current_folder, my_jars, URLS_IMDB, format_url_s3_downloads

# Percorre todos os modulos e cria as dags dinamicamente
for module in URLS_IMDB:
    with DAG(
            dag_id=f"ingest_{module}_dag",
            start_date=datetime(2022, 1, 1),
            schedule_interval=None,
            catchup=False) as dag:

        extract_csv = IMDBIngestToParquetOperator(
            task_id=f'ingest_{module}_task',
            conn_id='spark_awari',
            s3_url=format_url_s3_downloads(module),
            foldername=f"{module}/{current_folder}"
        )

        # TASKS
        extract_csv




# Example using SPARK SUBMIT, only for learning purposes!
dag1 = DAG(dag_id=f"spark_submit_ing_name_basics_dag", start_date=datetime(2021, 1, 1), schedule_interval=None, catchup=False)
extract_csv = SparkSubmitOperator(
    application="/opt/airflow/dags/spark/imdb_pyspark_extract.py",
    conn_id='spark_awari',
    task_id='ingest_name_basics_task',
    jars=my_jars,
    dag=dag1,
    application_args=[
        '-u',
        format_url_s3_downloads('name_basics'),
        '-f', f"name_basics/{current_folder}",
        '-e', f"parquet",
    ]
)
# TASKS
extract_csv

