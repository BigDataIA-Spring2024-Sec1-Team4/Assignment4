""""
"""




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

def upload_to_s3(file_content, file_name):
    try:
        # Upload file content to S3 bucket
        s3.put_object(Bucket=S3_BUCKET_NAME, Key=file_name, Body=file_content)
        st.success("File uploaded successfully to S3!")
    except Exception as e:
        st.error(f"Failed to upload file to S3. Error: {e}")

def main():
    st.title("PDF File Uploader to S3")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.success("File selected successfully!")

        # Upload the file to S3
        upload_to_s3(uploaded_file.getvalue(), uploaded_file.name)

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

        # Dummy button
        if st.button("Dummy Button"):
            st.write("You clicked the Dummy Button!")

if __name__ == "__main__":
    main()
