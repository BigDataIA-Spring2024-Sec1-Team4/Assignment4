import streamlit as st
import boto3
import os
import requests


# Set up AWS credentials
AWS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
S3_BUCKET_NAME = 'your_bucket_name'

# Create S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# FastAPI service URL
FASTAPI_URL = "http://localhost:8000"
# Snowflake API service URL
SNOWFLAKE_API_URL = "http://localhost:8001"


def upload_to_s3(file_path):
    file_name = os.path.basename(file_path)
    try:
        # Upload file to S3 bucket
        s3.upload_file(file_path, S3_BUCKET_NAME, file_name)
        st.success("File uploaded successfully to S3!")
    except Exception as e:
        st.error(f"Failed to upload file to S3. Attempting to save locally. Error: {e}")
        save_locally(file_path)

def save_locally(file_path):
    # Save file to local directory
    local_dir = "local_files"
    os.makedirs(local_dir, exist_ok=True)
    dest_path = os.path.join(local_dir, os.path.basename(file_path))
    os.rename(file_path, dest_path)
    st.success(f"File saved locally: {dest_path}")

def main():
    st.title("PDF File Uploader to S3")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        temp_file_path = f"temp/{uploaded_file.name}"
        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully!")

        # Upload the file to S3
        upload_to_s3(temp_file_path)


        # Trigger Airflow pipeline if file uploaded successfully
        if st.button("Trigger Pipeline"):
            # Upload file to FastAPI service to trigger Airflow pipeline
            files = {'file': uploaded_file}
            response = requests.post(f"{FASTAPI_URL}/trigger_airflow", files=files)
            if response.status_code == 200:
                st.success("Pipeline triggered successfully!")
            else:
                st.error("Error triggering pipeline")

         # Invoke Snowflake API service to bring back results
        if st.button("Fetch Results from Snowflake"):
            query = "SELECT * FROM your_table"
            response = requests.get(f"{SNOWFLAKE_API_URL}/execute_query", params={"query": query})
            if response.status_code == 200:
                data = response.json()
                if data["status"] == "success":
                    results = data["data"]
                    st.write("Query Results:")
                    st.write(results)
                else:
                    st.error(f"Error executing query: {data['message']}")
            else:
                st.error("Error connecting to Snowflake API")


if __name__ == "__main__":
    main()
