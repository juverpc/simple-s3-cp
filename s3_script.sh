#!/bin/bash

#Variables
CSV=${1:-'./environment/dev/restaurant.csv'}
S3_BUCKET=$(grep -A0 'data_bucket:' ./environment/dev/config.yml | tail -n1); S3_BUCKET=${S3_BUCKET//*data_bucket: /}
MODEL_PATH=$(grep -A0 'model_path:' ./environment/dev/config.yml | tail -n1); MODEL_PATH=${MODEL_PATH//*model_path: /}
#**********************************************#

for RESTAURANT in $(cat ${CSV} | grep -v '#')
do  
    aws s3 cp s3://$S3_BUCKET/$MODEL_PATH/${RESTAURANT}/chal/ ./lambdas/${RESTAURANT}-chal/model/ --recursive
    aws s3 cp s3://$S3_BUCKET/$MODEL_PATH/${RESTAURANT}/champ/ ./lambdas/${RESTAURANT}-champ/model/ --recursive
    # aws s3 cp s3://juver-upload-to-s3/model/${restaurant}/chal/ ./lambdas/${restaurant}-chal/model/ --recursive
    # aws s3 cp s3://juver-upload-to-s3/model/${restaurant}/champ/ ./lambdas/${restaurant}-champ/model/ --recursive
    
done < ./environment/dev/restaurant.csv




