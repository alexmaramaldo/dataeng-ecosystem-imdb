import os


from airflow import DAG, settings
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.models import Connection
from datetime import datetime

def create_aws_variables():
    """

    :return: Null
    :rtype:
    """
    print("Creating variables: AWS_ACCESS_KEY_ID, AWS_ENDPOINT, AWS_DEFAULT_REGION, AWS_SECRET_ACCESS_KEY, AWS_S3_IMDB_BUCKET")

    Variable.set("AWS_ENDPOINT", os.getenv("AWS_ENDPOINT"))
    Variable.set("AWS_ACCESS_KEY_ID", os.getenv("AWS_ACCESS_KEY_ID"))
    Variable.set("AWS_SECRET_ACCESS_KEY", os.getenv("AWS_SECRET_ACCESS_KEY"))
    Variable.set("AWS_DEFAULT_REGION", os.getenv("AWS_DEFAULT_REGION"))
    Variable.set("AWS_S3_IMDB_BUCKET", os.getenv("AWS_S3_IMDB_BUCKET"))

    print("Variables createds")

def create_spark_conn():
    print("Creating SPARK CONN to dataeng-spark-master docker container")
    conn = Connection(
        conn_id='spark_awari',
        conn_type='spark',
        host='spark://dataeng-spark-master',
        port='7077'
    )  # create a connection object
    session = settings.Session()  # get the session
    session.add(conn)
    session.commit()  # it will insert the connection object programmatically.

    print("Connection with Spark created")

def create_pg_conn():
    print("Creating PG CONN to dataeng-postgres docker container")
    conn = Connection(
        conn_id='pg_awari',
        conn_type='postgres',
        host='dataeng-postgres',
        login='postgres',
        password='postgres',
        port='5432'
    )  # create a connection object
    session = settings.Session()  # get the session
    session.add(conn)
    session.commit()  # it will insert the connection object programmatically.

    print("Connection with Postgres created")


dag =  DAG(
    dag_id=f"load_setup_dag",
    start_date=datetime(2021,1,1),
    schedule_interval='@once', 
    catchup=False)
      
variables_task = PythonOperator(
    task_id="create_aws_variables_task",
    python_callable=create_aws_variables,
    dag=dag
)

spark_conn_task = PythonOperator(
    task_id="create_spark_conn_task",
    python_callable=create_spark_conn,
    dag=dag
)

pg_conn_task = PythonOperator(
    task_id="create_pg_conn_task",
    python_callable=create_pg_conn,
    dag=dag
)


variables_task >> spark_conn_task >> pg_conn_task