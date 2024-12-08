# delete_store.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# SQL statements to drop tables
drop_tables_sql = """
-- Drop the reviews table first because it's dependent on the other tables
DROP TABLE IF EXISTS reviews CASCADE;

-- Drop the payments table
DROP TABLE IF EXISTS payments CASCADE;

-- Drop the order_items table
DROP TABLE IF EXISTS order_items CASCADE;

-- Drop the orders table
DROP TABLE IF EXISTS orders CASCADE;

-- Drop the products table
DROP TABLE IF EXISTS products CASCADE;

-- Drop the customers table
DROP TABLE IF EXISTS customers CASCADE;
"""

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

    # Execute drop table statements
    cur.execute(drop_tables_sql)
    print("Old e-commerce store tables deleted successfully.")

    # Commit the transaction to ensure changes are applied
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
