import os

import boto3
from dotenv import load_dotenv

load_dotenv()

S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_REGION_NAME = os.getenv("S3_REGION_NAME")
BUCKET_NAME = os.getenv("BUCKET_NAME")
DOWNLOAD_DIR = 'bucket_files'


def download_all_files(bucket_name, download_directory):
    s3 = boto3.client('s3',
                      aws_access_key_id=S3_ACCESS_KEY,
                      aws_secret_access_key=S3_SECRET_KEY,
                      region_name=S3_REGION_NAME)

    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    objects = s3.list_objects(Bucket=bucket_name)
    for obj in objects.get('Contents', []):
        file_name = obj['Key']
        local_file_path = os.path.join(download_directory, file_name)
        local_file_directory = os.path.dirname(local_file_path)
        if not os.path.exists(local_file_directory):
            os.makedirs(local_file_directory)
        s3.download_file(bucket_name, file_name, local_file_path)


if __name__ == '__main__':
    download_all_files(BUCKET_NAME, DOWNLOAD_DIR)
