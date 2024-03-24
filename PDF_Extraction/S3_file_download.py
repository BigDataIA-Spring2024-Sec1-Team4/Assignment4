import re
import os
from dotenv import load_dotenv
import boto3

# Load environment variables from .env file
def load_env():
    load_dotenv()
    #grobid_url = os.getenv("GROBID_URL")
    pdf_directory = os.getenv('PDF_DIR_PATH') # Store the downloaded PDF files from S3
    
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    
    
    return pdf_directory, output_dir, S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

pdf_directory, output_dir, S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY = load_env()




def download_files_from_s3():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # List objects in the specified S3 folder
    response = s3.list_objects_v2(Bucket=S3_BUCKET_NAME)

    if not os.path.exists(pdf_directory):
        os.makedirs(pdf_directory)


    # Download each file to the local directory
    #for obj in response.get('Contents')[1:]:
    for obj in response.get('Contents', []):
        key = obj['Key']
        print(key)
        local_file_path = os.path.join(pdf_directory, os.path.basename(key))
        print(local_file_path)

        try:
            s3.download_file(S3_BUCKET_NAME, key, local_file_path)
            print(f"Downloaded: {key} to {local_file_path}")
        except Exception as e:
            print(f"Failed to download {key}: {e}")
            

try:
    download_files_from_s3()
except Exception as e:
    print(f"An error occurred: {e}")
