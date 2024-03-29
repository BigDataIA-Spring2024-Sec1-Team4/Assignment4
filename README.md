
## Assignment 3
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



##  Prerequisites 



**General Software Prerequisites:**

1. **Python:** Install Python programming language (version 3.x) from the official Python website or using package managers like Anaconda.

2. **Snowflake Account:** Sign up for a Snowflake account or gain access to an existing account with appropriate permissions.

3. **Git:** Install Git version control system for managing project codebase.

   - Download and install Git from the official website: [Git](https://git-scm.com/)
  
 
## Project Structure




## Architectural Diagram

![image](https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment3/assets/114356265/bcd1c1a6-1afb-4de2-a49c-c76ba75b202c)



## How to run Application locally

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
     
4. **Host Grobid Server**: Open Docker Desktop and host the Grobid server. (Run this in a separate terminal)

   ```bash
    docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0
   ```

5. **Run the Execute Script**: Execute the `execute_commands.py` python script to run the application. This step automates the process and runs all scripts one after the other (Remember to add your .env files)

   ```bash
   python execute_commands.py
   ```

6. **Git Clone Astro**: This is required to run DBT Cloud on Airflow

   ```bash
   brew install astro
   git clone https://github.com/sungchun12/airflow-dbt-cloud.git
   ```
7. **Transfer the dag file into Airflow Directory**: Transfer dag script into the dag folder created through git clone

   ```bash
   python file_move.py
   ```
8. **Run Astro Airflow to run DBT Cloud jobs**: This will run both development and production jobs on DBT Cloud through Airflow. Don't forget to add DBT Cloud API in Airflow connection (conn_id = dbt_cloud)

   ```bash
   cd airflow-dbt-cloud
   astro dev start
   ```

Ensure that all software prerequisites are installed and configured properly before starting the project to avoid any issues during development and execution.



## Team Information and Contribution 

Name           | NUID          |
---------------|---------------|
Anirudh Joshi  | 002991365     |      
Nitant Jatale  | 002776669     |      
Rutuja More    | 00272782      |      
