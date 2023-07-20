from airflow.models.baseoperator import BaseOperator
from hooks.spark_hook import SparkHook
from airflow.models import Variable

class IMDBIngestToParquetOperator(BaseOperator):
    def __init__(self, conn_id: str, s3_url: str, foldername: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.s3_url = s3_url
        self.foldername = foldername
        self.spark_hook = SparkHook(conn_id=self.conn_id)

        self.spark = self.spark_hook.get_spark_context()

    def execute(self, context):
        self.process_to_parquet()

    def process_to_parquet(self):
        print("Spark S3 Setup")
        print(Variable.get("AWS_S3_IMDB_BUCKET"),
              Variable.get("AWS_ENDPOINT"),
              Variable.get("AWS_ACCESS_KEY_ID"),
              Variable.get("AWS_SECRET_ACCESS_KEY"),
              Variable.get("AWS_DEFAULT_REGION"))
        print(f"URL: |{self.s3_url}|")

        raw_df = self.spark.read.csv(self.s3_url, sep=r'\t', header=True)
        print("Schema from CSV")
        raw_df.printSchema()
        print("=====================")
        raw_df.write.parquet(f's3a://{Variable.get("AWS_S3_IMDB_BUCKET")}/datalake/{self.foldername}/data', mode='overwrite')
