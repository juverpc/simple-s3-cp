#!/bin/bash

CSV=${1:-'restaurant.csv'}

for line in $(cat ${CSV} | grep -v '#')
do
    folder="$(echo $line | cut -d , -f 1)"    
    aws s3 cp s3://juver-upload-to-s3/model2/${folder}/ ${CODEBUILD_SRC_DIR}/lambdas/${folder}/model/ --recursive 
    echo ${bucket_path} ${file_location}
done
