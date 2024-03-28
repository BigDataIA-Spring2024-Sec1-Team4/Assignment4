from fastapi import FastAPI, HTTPException
import requests
from requests.auth import HTTPBasicAuth
from pydantic import BaseModel
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

airflow_endpoint = os.getenv('airflowurl')

# Define a request model to expect certain JSON payload structure
class TriggerDAGRequest(BaseModel):
    dag_id: str
    conf: dict = None  # Optional configuration for the DAG

# Endpoint to trigger an Airflow DAG
@app.post("/trigger-airflow-dag")
async def trigger_airflow_dag(request_data: TriggerDAGRequest):
    airflow_url = f"{airflow_endpoint}/api/v1/dags/{request_data.dag_id}/dagRuns"
    # airflow_url = f"http://localhost:8080/api/v1/dags/grobid_processing/dagRuns"
    airflow_username = os.getenv('AIRFLOW_USERNAME')
    airflow_password = os.getenv('AIRFLOW_PASSWORD')
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    unique_run_id = f"triggered_via_fastapi_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    payload = {
        "dag_run_id": unique_run_id,
        "conf": request_data.conf if request_data.conf else {},
    }
    
    response = requests.post(
        airflow_url, 
        json=payload, 
        headers=headers,
        auth=HTTPBasicAuth(airflow_username, airflow_password)
    )
    
    if response.status_code in [200, 201]:
        return {"message": "DAG triggered successfully", "details": response.json()}
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
