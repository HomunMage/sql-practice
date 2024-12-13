# update_delete.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# SQL queries for updating and deleting data
update_sql = """
-- Update the status of order 1 to 'Shipped'
UPDATE orders
SET status = 'Shipped'
WHERE order_id = 1;

-- Update the price of the Laptop product
UPDATE products
SET price = 1099.99
WHERE product_id = 1;
"""

delete_sql = """
-- Delete order 1 and its associated items
DELETE FROM order_items WHERE order_id = 1;
DELETE FROM orders WHERE order_id = 1;

-- Delete the review for product 1
DELETE FROM reviews WHERE product_id = 1 AND customer_id = 1;
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

    # Perform updates
    cur.execute(update_sql)
    print("Data updated successfully.")

    # Perform deletions
    cur.execute(delete_sql)
    print("Data deleted successfully.")

    # Commit the transaction to save changes
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
