import streamlit as st
from snowflake_connector import snowflake
from dotenv import load_dotenv
import os
import openai

# Set your OpenAI API key
openai.api_key = os.getenv('openai_api_key')


# Fetch table names from the Snowflake database
def get_table_names():
    sql = "SHOW TABLES;"
    result = snowflake.execute_sql(sql)
    return result.iloc[:, 1].tolist()


def display_table_data(table_name):
    sql = f"SELECT * FROM {table_name}"
    table_data = snowflake.execute_sql(sql)
    st.write(f"First 5 rows of {table_name}:")
    st.write(table_data)


def generate_sql_query(prompt,selected_table):
    # Generate SQL query using OpenAI's text completion API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Change the model name if needed
        messages=[{"role": "system", "content": prompt + f" from {selected_table}"}],
        temperature=0.5,  
        max_tokens=150,   
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=[";"]
    )
    sql_query = response.choices[0].message["content"].strip()
    generated_sql_query = extract_sql_query(sql_query)
    return generated_sql_query


def extract_sql_query(sql_query):
    # Split the output by newline characters
    lines = sql_query.split('\n')
    
    # Find the index of the line containing "SELECT"
    select_index = None
    for i, line in enumerate(lines):
        if "SELECT" in line:
            select_index = i
            break
    
    # If "SELECT" is found, concatenate lines from that point till the end
    if select_index is not None:
        cleaned_sql_query = '\n'.join(lines[select_index:])
        return cleaned_sql_query.strip()
    else:
        return None

   

def main():
    st.title("Snowflake Table Viewer")
    table_names = get_table_names()
    selected_table = st.selectbox("Select a table:", table_names)
    if selected_table:
        display_table_data(selected_table)


    # Text area for user prompt
    prompt = st.text_area("Enter your prompt:", height=100)
    
    # Generate SQL query based on user prompt
    if st.button("Generate SQL"):
        sql_query = generate_sql_query(prompt,selected_table)
        st.write("Generated SQL Query:")
        st.code(sql_query, language="sql")
        new_sql_query = str(sql_query)

        st.session_state.generated_sql_query = new_sql_query  # Store generated SQL query

    # Execute SQL query and display results
    if st.button("Execute SQL"):
        if "generated_sql_query" in st.session_state:  # Check if SQL query exists
            sql_query = st.session_state.generated_sql_query
            table_data = snowflake.execute_sql(sql_query)
            st.write(f"Query Results:")
            st.write(table_data)
        
    
if __name__ == "__main__":
    main()