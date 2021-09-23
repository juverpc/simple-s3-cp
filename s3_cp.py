import boto3
import os
import tempfile
import yaml
from yaml import Loader

#WORK
def download_object():
    with open("./environment/dev/config.yml", 'r') as stream:
        get_config = yaml.load(stream,Loader=Loader)
        data_bucket= (get_config['data_bucket'])
        model_path= (get_config['model_path'])
    s3=boto3.client('s3')
    response = s3.list_objects_v2(Bucket=data_bucket, Prefix=f'{model_path}/restaurant1/challenger_model/stand_menu_2ac31518-47bb-4951-ba8c-c3f058193535/')
    s3_objects = [obj['Key'] for obj in response['Contents']]
    for s3_file in s3_objects:
        s3.download_file(data_bucket,s3_file,'./lambdas/restaurant1-chal/model/')

if __name__ == "__main__":
    download_object()