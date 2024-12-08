# print_all.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# Connect to PostgreSQL database
try:
    # Connect to the database
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    print("Connected to the database successfully!")

    # Create a cursor object
    cur = conn.cursor()

    # Step 1: Fetch all student records
    cur.execute("SELECT * FROM student_scores;")
    students = cur.fetchall()

    # Step 2: Print all student records
    print("All Student Records:")
    if students:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Score: {student[2]}")
    else:
        print("No student records found.")

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
