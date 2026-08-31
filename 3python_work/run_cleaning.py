import mysql.connector

import mysql.connector

def run_sql_file(filename):
    # Connect to our database
    conn = mysql.connector.connect(
        host="localhost",
        user="ecom_user",
        password="Password",   
        database="project"     
    )
    cursor = conn.cursor()

    with open(filename, "r") as f:
        sql_commands = f.read().split(";")

    for command in sql_commands:
        command = command.strip()
        if command:  
            try:
                cursor.execute(command)

                # If it's a SELECT, fetch results to clear buffer
                if command.lower().startswith("select"):
                    rows = cursor.fetchall()
                    print(f"Executed SELECT, {len(rows)} rows returned.")
                else:
                    conn.commit()
                    print(f"Executed: {command[:50]}...")

            except Exception as e:
                print(f"Error executing command:\n{command}\n{e}")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    run_sql_file("2sql/03_data_cleaning.sql")
    print("Data cleaning completed.")
