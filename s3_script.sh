#!/bin/bash

CSV=${1:-'restaurant.csv'}

#Chal
for restaurant in $(cat ${CSV} | grep -v '#')
do  
    aws s3 cp s3://juver-upload-to-s3/model2/${restaurant}/chal/ ./lambdas/${restaurant}-chal --recursive 
    
done

#Champ
for restaurant in $(cat ${CSV} | grep -v '#')
do  
    aws s3 cp s3://juver-upload-to-s3/model2/${restaurant}/champ/ ./lambdas/${restaurant}-champ --recursive 
    
done


