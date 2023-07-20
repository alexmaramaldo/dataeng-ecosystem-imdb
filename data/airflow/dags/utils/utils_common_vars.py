from airflow.models import Variable

from datetime import datetime
import glob
import os

current_time = datetime.now()
current_date = current_time .strftime("%Y-%m-%d")
year = current_time .strftime("%Y")
month = current_time .strftime("%m")
day = current_time .strftime("%d")
current_folder = f"year={year}/month={month}/day={day}"

mypath = "/opt/airflow/spark_jars"
files = glob.glob(f'{mypath}/*')
my_jars = ','.join(files)

URLS_IMDB = {
   'name_basics': 'https://datasets.imdbws.com/name.basics.tsv.gz',
   'title_akas': 'https://datasets.imdbws.com/title.akas.tsv.gz',
   'title_basics': 'https://datasets.imdbws.com/title.basics.tsv.gz',
   'title_crew': 'https://datasets.imdbws.com/title.crew.tsv.gz',
   'title_episode': 'https://datasets.imdbws.com/title.episode.tsv.gz',
   'title_principals': 'https://datasets.imdbws.com/title.principals.tsv.gz',
   'title_ratings': 'https://datasets.imdbws.com/title.ratings.tsv.gz'
}


def format_url_s3_downloads(module):
   url = f"s3a://{Variable.get('AWS_S3_IMDB_BUCKET')}/downloaded/{module}/{current_folder}/{os.path.basename(URLS_IMDB[module])}"
   return url