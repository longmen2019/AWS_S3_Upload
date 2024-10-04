import os
import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Read from environment variables instead of hardcoding
AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME", "eagleimagebucket")
AWS_REGION = os.getenv("AWS_REGION ", "us-east-2")

logging.basicConfig(level=logging.INFO)
LOCAL_FILE = 'eaglesoaring.jpg'
NAME_FOR_S3 = 'eaglesoaring.jpg'


def upload_file_to_s3(local_file: str, bucket_name: str, s3_file_name: str) -> None:
    try:
        # Use boto3.Session to manage credentials more securely and flexibly
        session = boto3.Session(
            region_name=AWS_REGION,
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
        )
        s3_client = session.client('s3')
        response = s3_client.upload_file(LOCAL_FILE, bucket_name, s3_file_name)
        logging.info(f'upload file response: {response}')
    except NoCredentialsError:
        logging.error('Credentials not available')
    except PartialCredentialsError:
        logging.error('Incomplete credentials provided')
    except ClientError as e:
        logging.error(f'Client error: {e}')
    except FileNotFoundError as e:
        logging.error(f'File not found: {e}')
    except Exception as e:
        logging.error(f'A error occurred: {e}')


def main():
    upload_file_to_s3(LOCAL_FILE, AWS_S3_BUCKET_NAME, NAME_FOR_S3)


if __name__ == '__main__':
    main()
