#!/bin/bash

#Variables
#CSV=${1:-'./environment/dev/restaurant.csv'}


DATA_BUCKET=$(grep -A0 'data_bucket:' ./environment/dev/config.yml | tail -n1); DATA_BUCKET=${DATA_BUCKET//*data_bucket: /}
MODEL_PATH=$(grep -A0 'model_path:' ./environment/dev/config.yml | tail -n1); MODEL_PATH=${MODEL_PATH//*model_path: /}

for RESTAURANT in $(cat ${CSV} | grep -v '#')
do  

    aws s3 cp s3://$DATA_BUCKET/$MODEL_PATH/${RESTAURANT}/chal/ ./lambdas/${RESTAURANT}-chal/model/ --recursive
    aws s3 cp s3://$DATA_BUCKET/$MODEL_PATH/${RESTAURANT}/champ/ ./lambdas/${RESTAURANT}-champ/model/ --recursive
        
done < ./environment/dev/restaurant.csv




