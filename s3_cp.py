import boto3
import os
import tempfile
import yaml
from yaml import Loader

# S3_BUCKET = "juver-upload-to-s3"
# S3_PREFIX = "auto_training_pipeline/sm_pipelines/deployed_models/restaurant1/challenger_model/stand_menu_2ac31518-47bb-4951-ba8c-c3f058193535/"

# def download_object():
#     #with tempfile.TemporaryDirectory() as tempdir:
#     local_path= './lambdas/restaurant1-chal/model/'
#     s3 = boto3.client('s3')
#     response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
#     s3_objects = [obj['Key'] for obj in response['Contents']]
#     for s3_file in s3_objects:
#         local_file_path = os.path.join(local_path, s3_file.replace(S3_PREFIX, ""))
#         s3.download_file(S3_BUCKET, s3_file, local_file_path)
#     print(f"Downloaded files: {', '.join(os.listdir(local_path))}")
#WORK
def download_object():
    with open("./environment/dev/config.yml", 'r') as stream:
        get_config = yaml.load(stream,Loader=Loader)
        data_bucket= (get_config['data_bucket'])
        model_path= (get_config['model_path'])
    s3=boto3.client('s3')
    prefix_s3= f'{model_path}/restaurant1/challenger_model/stand_menu_2ac31518-47bb-4951-ba8c-c3f058193535/'
    response = s3.list_objects_v2(Bucket=data_bucket, Prefix=prefix_s3)
    s3_objects = [obj['Key'] for obj in response['Contents']]
    for s3_file in s3_objects:
        local_file_path = os.path.join('./lambdas/restaurant1-chal/model/', s3_file.replace(prefix_s3, ""))
        s3.download_file(data_bucket, s3_file, local_file_path)

if __name__ == "__main__":
    download_object()