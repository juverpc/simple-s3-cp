import boto3
import os
import tempfile

S3_BUCKET = "juver-upload-to-s3"
S3_PREFIX = "auto_training_pipeline/sm_pipelines/deployed_models/restaurant1/challenger_model/stand_menu_2ac31518-47bb-4951-ba8c-c3f058193535/"

def download_object():
    #with tempfile.TemporaryDirectory() as tempdir:
    local_path= './lambdas/restaurant1-chal/model/'
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
    s3_objects = [obj['Key'] for obj in response['Contents']]
    for s3_file in s3_objects:
        local_file_path = os.path.join(local_path, s3_file.replace(S3_PREFIX, ""))
        s3.download_file(S3_BUCKET, s3_file, local_file_path)
    print(f"Downloaded files: {', '.join(os.listdir(local_path))}")
#WORK
# def download_object():
#     s3=boto3.client('s3')
#     s3.download_file('juver-upload-to-s3', 'auto_training_pipeline/sm_pipelines/deployed_models/restaurant1/challenger_model/stand_menu_2ac31518-47bb-4951-ba8c-c3f058193535/model.tar.gz', './lambdas/restaurant1-chal/model/model.tar.gz')

if __name__ == "__main__":
    download_object()