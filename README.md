
## Assignment 4
Automated PDF Data Extraction and Querying Pipeline with Airflow and Snowflake Integration


## Problem Statement:

Develop an end-to-end pipeline utilizing Airflow to automate the extraction and storage of meta-data and content from PDF files into Snowflake. The task involves building two API services using FastAPI: one to trigger the Airflow pipeline and another to interface with Snowflake for querying.


## Project Goals

  1.Build a FastAPI service to accept S3 file locations and initiate an Airflow pipeline for:
    a. Extraction of data and metadata from PDF files.
    b. Validating the extracted data using predefined tools.
    c. Loading the data and metadata into Snowflake.

  2.Develop a separate FastAPI service to interact with Snowflake and provide query responses.


## Codelab

[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1H-NznhIh2AqN8jsjyq399n_NODPnIhcgUE6CWyrsULI#5)

[Demo](https://www.youtube.com/watch?v=ilUbDRxwoWw&ab_channel=AnirudhaJoshi)

## Technologies Used

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-387BC3?style=for-the-badge&logo=snowflake&logoColor=light)](https://www.snowflake.com/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-59666C?style=for-the-badge&logo=python&logoColor=blue)](https://www.crummy.com/software/BeautifulSoup/)
[![Grobid](https://img.shields.io/badge/Grobid-007396?style=for-the-badge&logo=java&logoColor=white)](https://github.com/kermitt2/grobid)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)
[![Google Cloud Platform](https://img.shields.io/badge/Google%20Cloud%20Platform-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://www.streamlit.io/)
[![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)](https://aws.amazon.com/s3/)



## Project Structure




## Architectural Diagram

![image](https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment3/assets/114356265/bcd1c1a6-1afb-4de2-a49c-c76ba75b202c)



## To run the application locally, follow these steps:

1. **Clone the Repository**: Clone the repository onto your local machine.

   ```bash
   git clone https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment3
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**: Activate the virtual environment.

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS**:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**: Navigate to the project directory and install the required dependencies.

   ```bash
   cd Assignment3
   pip install -r requirements.txt
   ```

5. **Run Docker Compose**: Start the Docker containers using Docker Compose.

   ```bash
   docker-compose up -d
   ```

6. **Access Streamlit Interface**: Open your web browser and go to `localhost:8000` to access the Streamlit interface.

7. **Upload PDF to S3**: On the Streamlit homepage, upload a PDF file to S3. After successful upload, trigger the Airflow pipeline.

8. **Fetch Results**: Navigate to the "Fetch Result" page on the Streamlit interface. Select a table from which you want to retrieve data from Snowflake. Write a prompt and click on "Generate SQL Query". Review the generated SQL query and edit if necessary. Finally, click on "Execute Query" to retrieve the desired data from the Snowflake table.

By following these steps, you should be able to run the application locally and interact with it using the provided Streamlit interface to upload PDF files, trigger data processing pipelines, and query Snowflake for results.


## Team Information and Contribution 

Name           | NUID          |
---------------|---------------|
Anirudh Joshi  | 002991365     |      
Nitant Jatale  | 002776669     |      
Rutuja More    | 00272782      |      
