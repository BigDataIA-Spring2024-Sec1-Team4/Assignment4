import streamlit as st
import snowflake.connector
import pandas as pd

# Snowflake connection details
SNOWFLAKE_ACCOUNT = "your_account_name"
SNOWFLAKE_USERNAME = "your_username"
SNOWFLAKE_PASSWORD = "your_password"
SNOWFLAKE_DATABASE = "your_database"
SNOWFLAKE_SCHEMA = "your_schema"

# Function to execute query and return results as DataFrame
def execute_query(query):
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USERNAME,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(data, columns=columns)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error executing query: {str(e)}")

# Streamlit app
def main():
    st.title("Snowflake Data Explorer")

    # Data selection
    selected_tables = st.multiselect("Select tables:", ["table1", "table2", "table3"])

    # Show selected tables
    if selected_tables:
        st.write(f"Selected tables: {', '.join(selected_tables)}")

        # Data preview
        query = f"SELECT * FROM {' ,'.join(selected_tables)} LIMIT 10"
        st.write("Data Preview:")
        data_preview = execute_query(query)
        st.write(data_preview)

        # Aggregation and Grouping
        aggregation_func = st.selectbox("Select aggregation function:", ["SUM", "AVG", "COUNT", "MIN", "MAX"])
        selected_column = st.selectbox("Select column for aggregation:", data_preview.columns)
        if aggregation_func and selected_column:
            query = f"SELECT {aggregation_func}({selected_column}) FROM {' ,'.join(selected_tables)}"
            st.write("Aggregated Result:")
            aggregated_result = execute_query(query)
            st.write(aggregated_result)

        # Visualization
        if st.button("Visualize Data"):
            st.write("Visualizations will appear here.")

if __name__ == "__main__":
    main()
