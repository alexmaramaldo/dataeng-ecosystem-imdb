from airflow.hooks.base import BaseHook
from airflow.models import Variable

from utils.utils_common_vars import my_jars

from pyspark.sql import SparkSession

class SparkHook(BaseHook):
    def __init__(self, conn_id: str, **kwargs) -> None:
        super().__init__()
        self.conn_id = conn_id
        self.conn = self.get_connection(self.conn_id)

        self.spark = SparkSession \
            .builder \
            .appName("AirFlowDataExtraction") \
            .config("spark.jars", my_jars) \
            .master(f"{self.conn.host}:{self.conn.port}") \
            .getOrCreate()
        self.setupHadoop()

    def get_uri(self):
        return self.conn.uri()

    def setupHadoop(self):
        hadoop_conf = self.spark.sparkContext._jsc.hadoopConfiguration()
        if Variable.get("AWS_ENDPOINT") != 'null':
            hadoop_conf.set("fs.s3a.endpoint", Variable.get("AWS_ENDPOINT"))
            hadoop_conf.set("fs.s3a.connection.ssl.enabled", "false")

        hadoop_conf.set("fs.s3a.endpoint.region", Variable.get("AWS_DEFAULT_REGION"))
        hadoop_conf.set("fs.s3a.access.key", Variable.get('AWS_ACCESS_KEY_ID'),)
        hadoop_conf.set("fs.s3a.secret.key", Variable.get('AWS_SECRET_ACCESS_KEY'))
        hadoop_conf.set("fs.s3a.path.style.access", "true")
        # hadoop_conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
        hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

    def get_spark_context(self):
        return self.spark

