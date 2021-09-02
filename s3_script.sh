#!/bin/bash

CSV=${1:-'restaurant.csv'}

#Chal
for line in $(cat ${CSV} | grep -v '#')
do
    restaurant="$(echo $line | cut -d , -f 1)"    
    aws s3 cp s3://juver-upload-to-s3/model2/${restaurant}/chal/ ./lambdas/${restaurant}-chal/model/ --recursive 
    
done

#Champ
for line in $(cat ${CSV} | grep -v '#')
do
    restaurant="$(echo $line | cut -d , -f 1)"    
    aws s3 cp s3://juver-upload-to-s3/model2/${restaurant}/champ/ ./lambdas/${restaurant}-champ/model/ --recursive 
    
done
