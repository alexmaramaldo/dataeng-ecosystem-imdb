import requests
import json
from pyspark.sql import SparkSession
from pyspark import SQLContext
from pyspark.sql import functions as F
from decouple import config
import getopt
import sys
 
fileurl=""
foldername=""
export_format="csv"
argv = sys.argv[1:]
try:
    options, args = getopt.getopt(argv, "u:f:e:",
                               ["url=",
                                "folder=",
                                "export="])
except:
    print("Error Message ")
 
for name, value in options:
    if name in ['-u', '--url']:
        fileurl = value
    elif name in ['-f', '--folder']:
        foldername = value
    elif name in ['-e', '--export']:
        export_format = value
print("FILEURL", fileurl)
print("FOLDERNAME", foldername)
print("FILE FORMAT", export_format)

aws_access_key = config('AWS_ACCESS_KEY_ID')
aws_secret_key = config('AWS_SECRET_ACCESS_KEY')

spark = SparkSession \
    .builder \
    .appName("DataExtraction") \
    .getOrCreate() 

hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.endpoint", 'http://dataeng-minio-nginx:9000')
hadoop_conf.set("fs.s3a.connection.ssl.enabled", "false")
hadoop_conf.set("fs.s3a.endpoint.region", 'sa-east-1')
hadoop_conf.set("fs.s3a.access.key", aws_access_key)
hadoop_conf.set("fs.s3a.secret.key", aws_secret_key)
hadoop_conf.set("fs.s3a.path.style.access", "true")
# hadoop_conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

raw_json_dataframe = spark.read.csv(fileurl, sep=r'\t', header=True)

raw_json_dataframe.printSchema()

if export_format == 'csv':
    raw_json_dataframe.write.format('csv').option('header','true').save(f's3a://watch-ops-plataform/datalake/{foldername}',mode='overwrite')
else:
    raw_json_dataframe.write.parquet(f's3a://watch-ops-plataform/datalake/{foldername}/data',mode='overwrite')