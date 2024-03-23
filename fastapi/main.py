"""from fastapi import FastAPI
from airflow.dags.pdf_processing_dags import pdf_processing_dag 
app = FastAPI()

@app.post("/trigger_airflow")
async def trigger_airflow(s3_location: str):
    # Code to trigger Airflow pipeline
    print(f"Triggering Airflow pipeline for S3 location: {s3_location}")
    return {"message": "Airflow pipeline triggered successfully"}



@app.post("/trigger_airflow")
async def trigger_airflow(s3_location: str, local_location: str = None):
    if s3_location:
        # Code to trigger Airflow pipeline for S3 location

        
        print(f"Triggering Airflow pipeline for S3 location: {s3_location}")
    elif local_location:
        # Code to trigger Airflow pipeline for local file location
        print(f"Triggering Airflow pipeline for local file location: {local_location}")
    else:
        return {"error": "No file location provided"}

    return {"message": "Airflow pipeline triggered successfully"}"""



from fastapi import FastAPI
from airflow import DAG, settings, dags
from airflow.models import DagBag
from airflow.api.client.local_client import Client

app = FastAPI()

# Initialize the Airflow DAG
dagbag = DagBag(settings.DAGS_FOLDER)
dag_id = 'pdf_processing_pipeline'

if dag_id not in dagbag.dags:
    raise ValueError(f"DAG '{dag_id}' not found in DAG folder.")

@app.post("/trigger_airflow")
async def trigger_airflow(s3_location: str, local_location: str = None):
    if s3_location:
        # Trigger Airflow pipeline for S3 location
        client = Client(None, None)
        client.trigger_dag(dag_id, run_id=f"S3_{s3_location}")
        return {"message": f"Airflow pipeline triggered successfully for S3 location: {s3_location}"}
    elif local_location:
        # Trigger Airflow pipeline for local file location
        client = Client(None, None)
        client.trigger_dag(dag_id, run_id=f"Local_{local_location}")
        return {"message": f"Airflow pipeline triggered successfully for local file location: {local_location}"}
    else:
        return {"error": "No file location provided"}
