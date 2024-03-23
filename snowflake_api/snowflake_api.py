from fastapi import FastAPI, Query
import snowflake.connector

app = FastAPI()

# Snowflake connection parameters
SNOWFLAKE_ACCOUNT = 'your_account_name'
SNOWFLAKE_USER = 'your_username'
SNOWFLAKE_PASSWORD = 'your_password'
SNOWFLAKE_DATABASE = 'your_database_name'
SNOWFLAKE_WAREHOUSE = 'your_warehouse_name'

# Function to establish Snowflake connection
def get_snowflake_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE
    )

@app.get("/execute_query")
async def execute_query(query: str = Query(...)):
    try:
        # Execute the query
        conn = get_snowflake_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        
        # Fetch results
        results = cursor.fetchall()

        return {"status": "success", "data": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        if conn:
            conn.close()
