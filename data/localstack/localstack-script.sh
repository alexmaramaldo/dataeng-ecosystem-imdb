#!/bin/bash

awslocal s3api \
create-bucket --bucket dataeng-imdb \
--create-bucket-configuration LocationConstraint=eu-central-1 \
--region sa-east-1