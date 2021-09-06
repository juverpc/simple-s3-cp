#!/bin/bash

CSV=${1:-'restaurant.csv'}

for restaurant in $(cat ${CSV} | grep -v '#')
do  
    aws s3 cp s3://juver-upload-to-s3/model/${restaurant}/chal/ ./lambdas/${restaurant}-chal/model/ --recursive
    aws s3 cp s3://juver-upload-to-s3/model/${restaurant}/champ/ ./lambdas/${restaurant}-champ/model/ --recursive
    
done < restaurant.csv




