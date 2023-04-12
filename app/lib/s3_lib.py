from tempfile import NamedTemporaryFile

import boto3
from botocore.exceptions import ClientError
from celery.utils.log import get_task_logger
from flask import current_app as flask_app

from app.lib.constants import S3_LINK_EXPIRATION_LIMIT, S3_TEMPLATE_FOLDER
from app.lib.custom_exception import S3AWSDownloadException, S3AWSUploadException

celery_logger = get_task_logger(__name__)


def upload_file(file, folder, bucket=''):
    if not bucket:
        bucket = flask_app.config.get('S3_BUCKET')

    upload_file_name = f'{folder}/{file.filename}'
    flask_app.logger.info(f'Trying to upload {upload_file_name} to s3 bucket {bucket}.')
    celery_logger.info(f'Trying to upload {file.filename} to s3 bucket {bucket}.')
    s3_client = boto3.client(
        's3',
        aws_access_key_id=flask_app.config.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=flask_app.config.get('AWS_SECRET_ACCESS_KEY')
    )
    try:
        response = s3_client.upload_fileobj(file, bucket, upload_file_name)
    except ClientError as ex:
        error_msg = f'File upload failed {upload_file_name} to s3 bucket {bucket}.'
        flask_app.logger.error(f'{error_msg} | Error - {ex}')
        celery_logger.error(f'{error_msg} | Error - {ex}')
        raise S3AWSUploadException(error_msg)

    flask_app.logger.info(f'Successfully uploaded {upload_file_name} from s3 bucket {bucket}.')
    celery_logger.info(f'Successfully uploaded {upload_file_name} from s3 bucket {bucket}.')
    return response


def download_file(file_name, folder, bucket=''):
    if not bucket:
        bucket = flask_app.config.get('S3_BUCKET')

    download_file_name = f'{folder}/{file_name}'
    flask_app.logger.info(f'Trying to download {download_file_name} to s3 bucket {bucket}.')
    celery_logger.info(f'Trying to download {download_file_name} to s3 bucket {bucket}.')
    s3_client = boto3.client(
        's3',
        aws_access_key_id=flask_app.config.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=flask_app.config.get('AWS_SECRET_ACCESS_KEY')
    )
    try:
        data_file = s3_client.get_object(
            Bucket=bucket,
            Key=download_file_name
        )['Body'].read()
    except ClientError as ex:
        if ex.response['Error']['Code'] == "404":
            error_msg = f'File download failed. {download_file_name} does not exist at upload location.'
            flask_app.logger.error(f'{error_msg} | Error - {ex}')
            celery_logger.error(f'{error_msg} | Error - {ex}')
            raise S3AWSDownloadException(error_msg)

        raise S3AWSDownloadException(f'Error occurred while downloading file {download_file_name}')

    flask_app.logger.info(f'Successfully downloaded {download_file_name} from s3 bucket {bucket}.')
    celery_logger.info(f'Successfully downloaded {download_file_name} from s3 bucket {bucket}.')
    return data_file


def get_downloaded_file(file_name, folder, bucket=''):
    temp_file = NamedTemporaryFile()
    temp_file.name = file_name
    file_data = download_file(file_name, folder, bucket)
    temp_file.write(file_data)

    return temp_file


def get_presigned_download_url(file_name, folder=S3_TEMPLATE_FOLDER, bucket='', expiration=S3_LINK_EXPIRATION_LIMIT):
    if not bucket:
        bucket = flask_app.config.get('S3_BUCKET')

    download_file_name = f'{folder}/{file_name}'
    flask_app.logger.info(f'Trying to generate presigned url for file {download_file_name}')
    celery_logger.info(f'Trying to generate presigned url for file {download_file_name}')
    s3_client = boto3.client(
        's3',
        aws_access_key_id=flask_app.config.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=flask_app.config.get('AWS_SECRET_ACCESS_KEY'),
        config=boto3.session.Config(signature_version='s3v4'),
        region_name='us-east-2'
    )
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': download_file_name},
            ExpiresIn=expiration,
            HttpMethod="GET",
        )
        celery_logger.info(f'File - {download_file_name} | URL - {url}')
    except ClientError as ex:
        celery_logger.error(f'Error - {ex}')
        flask_app.logger.error(f'Error - {ex}')
        raise S3AWSDownloadException(f'Unable to create presigned url to download {download_file_name}')

    return url
