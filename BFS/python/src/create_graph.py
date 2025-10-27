# create_graph.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# SQL statements to create tables
create_graph_sql = """
-- Create Locations table (Nodes)
CREATE TABLE IF NOT EXISTS locations (
    location_id SERIAL PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    location_type VARCHAR(50) NOT NULL
);

-- Create Routes table (Edges)
CREATE TABLE IF NOT EXISTS routes (
    route_id SERIAL PRIMARY KEY,
    from_location_id INT REFERENCES locations(location_id) ON DELETE CASCADE,
    to_location_id INT REFERENCES locations(location_id) ON DELETE CASCADE,
    distance DECIMAL(10, 2),
    transport_time DECIMAL(10, 2),
    cost DECIMAL(10, 2)
);
"""

# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    print("Connected to the database successfully!")

    # Create a cursor object
    cur = conn.cursor()

    # Execute the table creation script
    cur.execute(create_graph_sql)
    print("Graph tables created successfully.")

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
