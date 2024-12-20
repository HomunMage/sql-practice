# delete_library.py
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

    # Step 1: Drop the existing tables if they exist
    cur.execute("DROP TABLE IF EXISTS BorrowingHistory;")
    cur.execute("DROP TABLE IF EXISTS Books;")
    cur.execute("DROP TABLE IF EXISTS Members;")
    cur.execute("DROP TABLE IF EXISTS Authors;")
    
    # Commit the transaction to drop the tables
    conn.commit()
    print("Existing library tables deleted successfully.")

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
