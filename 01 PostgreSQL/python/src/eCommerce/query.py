# query.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# SQL queries to retrieve data
query_sql = """
-- Get the order history for customer 1
SELECT o.order_id, o.order_date, o.status, oi.product_id, oi.quantity, oi.unit_price
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.customer_id = 1;

-- Get all products in the 'Electronics' category
SELECT * FROM products
WHERE category = 'Electronics';

-- Get reviews for the Laptop product
SELECT r.rating, r.review_text, r.review_date, c.first_name, c.last_name
FROM reviews r
JOIN customers c ON r.customer_id = c.customer_id
WHERE r.product_id = 1;
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

    # Execute queries and print results
    cur.execute(query_sql)
    results = cur.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
