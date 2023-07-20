FROM apache/airflow:2.2.5-python3.8

USER root

# Install OpenJDK-11
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

RUN apt-get install libpq-dev python-dev -y

RUN mkdir -p /opt/airflow/spark_jars_tmp
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.231/aws-java-sdk-bundle-1.12.231.jar --output /opt/airflow/spark_jars_tmp/aws-java-sdk-bundle-1.12.231.jar
RUN curl https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar --output /opt/airflow/spark_jars_tmp/hadoop-aws-3.3.1.jar
RUN curl https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.4/jets3t-0.9.4.jar --output /opt/airflow/spark_jars_tmp/jets3t-0.9.4.jar
RUN curl https://repo1.maven.org/maven2/joda-time/joda-time/2.12.2/joda-time-2.12.2.jar --output /opt/airflow/spark_jars_tmp/joda-time-2.12.2.jar
RUN curl https://repo1.maven.org/maven2/org/apache/httpcomponents/client5/httpclient5/5.2.1/httpclient5-5.2.1.jar --output /opt/airflow/spark_jars_tmp/httpclient5-5.2.1.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.400/aws-java-sdk-s3-1.12.400.jar --output /opt/airflow/spark_jars_tmp/aws-java-sdk-s3-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-kms/1.12.400/aws-java-sdk-kms-1.12.400.jar --output /opt/airflow/spark_jars_tmp/aws-java-sdk-kms-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-dynamodb/1.12.400/aws-java-sdk-dynamodb-1.12.400.jar --output /opt/airflow/spark_jars_tmp/aws-java-sdk-dynamodb-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-core/1.12.400/aws-java-sdk-core-1.12.400.jar --output /opt/airflow/spark_jars_tmp/aws-java-sdk-core-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.400/aws-java-sdk-1.12.400.jar --output /opt/airflow/spark_jars_tmp/aws-java-sdk-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.6/slf4j-api-2.0.6.jar --output /opt/airflow/spark_jars_tmp/slf4j-api-2.0.6.jar
RUN curl https://repo1.maven.org/maven2/org/slf4j/slf4j-reload4j/2.0.6/slf4j-reload4j-2.0.6.jar --output /opt/airflow/spark_jars_tmp/slf4j-reload4j-2.0.6.jar
RUN curl https://jdbc.postgresql.org/download/postgresql-42.6.0.jar --output /opt/airflow/spark_jars_tmp/postgresql-42.6.0.jar
USER airflow 

RUN pip3 install 'apache-airflow[amazon]' boto3
RUN pip3 install pyspark==3.3.0
RUN pip3 install apache-airflow-providers-apache-spark lxml python-decouple requests pandas
# RUN pip3 install psycopg2 

