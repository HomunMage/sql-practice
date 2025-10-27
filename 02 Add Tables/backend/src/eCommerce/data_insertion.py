# data_insertion.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# SQL statements to insert data
insert_data_sql = """
-- Insert some customers
INSERT INTO customers (first_name, last_name, email, phone_number, address) VALUES
('John', 'Doe', 'john.doe@example.com', '555-1234', '123 Elm Street'),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678', '456 Oak Avenue')
ON CONFLICT (email) DO NOTHING; -- Prevent inserting duplicates

-- Insert some products
INSERT INTO products (product_name, description, category, price, inventory_count) VALUES
('Laptop', 'High-performance laptop with 16GB RAM', 'Electronics', 999.99, 50),
('T-shirt', 'Cotton t-shirt, size M', 'Clothing', 19.99, 100),
('Headphones', 'Noise-cancelling wireless headphones', 'Electronics', 199.99, 30)
ON CONFLICT (product_name) DO NOTHING;

-- Insert an order for customer 1
INSERT INTO orders (customer_id, status) VALUES
(1, 'Pending');

-- Insert order items for the order with ID 1 (Laptop and Headphones)
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 999.99),  -- Laptop
(1, 3, 2, 199.99);  -- Headphones

-- Insert a payment for the order
INSERT INTO payments (order_id, payment_method, payment_amount) VALUES
(1, 'Credit Card', 1399.97);

-- Insert a review for the Laptop product by customer 1
INSERT INTO reviews (customer_id, product_id, rating, review_text) VALUES
(1, 1, 5, 'Amazing laptop, very fast and reliable!');
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

    # Insert the data
    cur.execute(insert_data_sql)
    print("Sample data inserted successfully.")

    # Commit the transaction to save changes
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
