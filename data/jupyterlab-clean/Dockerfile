FROM jupyter/datascience-notebook:python-3.8
USER root

# Add essential packages
RUN apt-get update && apt-get install -y \
    build-essential curl git gnupg2 nano apt-transport-https \ 
    openjdk-11-jdk and \
    software-properties-common

# Set locale
RUN apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

RUN mkdir -p /opt/spark_jars
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.231/aws-java-sdk-bundle-1.12.231.jar --output /opt/spark_jars/aws-java-sdk-bundle-1.12.231.jar
RUN curl https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar --output /opt/spark_jars/hadoop-aws-3.3.1.jar
RUN curl https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.4/jets3t-0.9.4.jar --output /opt/spark_jars/jets3t-0.9.4.jar
RUN curl https://repo1.maven.org/maven2/joda-time/joda-time/2.12.2/joda-time-2.12.2.jar --output /opt/spark_jars/joda-time-2.12.2.jar
RUN curl https://repo1.maven.org/maven2/org/apache/httpcomponents/client5/httpclient5/5.2.1/httpclient5-5.2.1.jar --output /opt/spark_jars/httpclient5-5.2.1.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.400/aws-java-sdk-s3-1.12.400.jar --output /opt/spark_jars/aws-java-sdk-s3-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-kms/1.12.400/aws-java-sdk-kms-1.12.400.jar --output /opt/spark_jars/aws-java-sdk-kms-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-dynamodb/1.12.400/aws-java-sdk-dynamodb-1.12.400.jar --output /opt/spark_jars/aws-java-sdk-dynamodb-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-core/1.12.400/aws-java-sdk-core-1.12.400.jar --output /opt/spark_jars/aws-java-sdk-core-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.400/aws-java-sdk-1.12.400.jar --output /opt/spark_jars/aws-java-sdk-1.12.400.jar
RUN curl https://repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.6/slf4j-api-2.0.6.jar --output /opt/spark_jars/slf4j-api-2.0.6.jar
RUN curl https://repo1.maven.org/maven2/org/slf4j/slf4j-reload4j/2.0.6/slf4j-reload4j-2.0.6.jar --output /opt/spark_jars/slf4j-reload4j-2.0.6.jar
# RUN curl https://repo1.maven.org/maven2/com/stratio/datasource/spark-mongodb_2.11/0.12.0/spark-mongodb_2.11-0.12.0.jar  --output /opt/spark_jars/spark-mongodb_2.11-0.12.0.jar
#RUN curl https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.13/10.2.0/mongo-spark-connector_2.13-10.2.0.jar --output /opt/spark_jars/mongo-spark-connector_2.13-10.2.0.jar
RUN curl https://jdbc.postgresql.org/download/postgresql-42.6.0.jar --output /opt/spark_jars/postgresql-42.6.0.jar
#RUN curl https://repo1.maven.org/maven2/org/mongodb/bson/4.9.1/bson-4.9.1.jar --output /opt/spark_jars/bson-4.9.1.jar
#RUN curl https://repo1.maven.org/maven2/org/mongodb/mongodb-driver/3.9.1/mongodb-driver-3.9.1.jar --output /opt/spark_jars/mongodb-driver-3.9.1.jar
#RUN curl https://repo1.maven.org/maven2/org/mongodb/mongodb-driver-core/4.9.1/mongodb-driver-core-4.9.1.jar --output /opt/spark_jars/mongodb-driver-core-4.9.1.jar

USER $NB_USER

# Install NLTK
RUN pip install nltk pyspark==3.3.0 boto3 python-decouple matplotlib pymongo

RUN which python
