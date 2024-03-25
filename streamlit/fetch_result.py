import streamlit as st
import requests

# Snowflake API service URL
SNOWFLAKE_API_URL = "http://localhost:8001"

def fetch_results_page():
    st.title("Fetch Results")

    # Add content for the page
    query = st.text_area("Enter your SQL query here:")
    if st.button("Execute Query"):
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

def main():
    fetch_results_page()

if __name__ == "__main__":
    main()
