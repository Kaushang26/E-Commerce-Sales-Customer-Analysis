import mysql.connector
import pandas as pd
import os

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="ecom_user",
        password="Password",
        database="project"
    )

def run_query(query, filename=None):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()

    if filename:
        # Ensure results/csv directory exists
        os.makedirs("results/csv", exist_ok=True)
        df.to_csv(f"results/csv/{filename}.csv", index=False)

    return df
