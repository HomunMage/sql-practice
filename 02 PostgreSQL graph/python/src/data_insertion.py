# data_insertion.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# SQL statements to insert data for BFS demonstration
insert_data_sql = """
-- Insert Locations (Nodes)
INSERT INTO locations (location_name, location_type) VALUES
('Factory A', 'Factory'),
('Warehouse B', 'Warehouse'),
('Warehouse C', 'Warehouse'),
('Store D', 'Store'),
('Store E', 'Store'),
('Distribution Hub F', 'Distribution Hub'),
('Retail Center G', 'Retail Center')
ON CONFLICT DO NOTHING;

-- Insert Routes (Edges)
INSERT INTO routes (from_location_id, to_location_id, distance, transport_time, cost) VALUES
(1, 2, 100.0, 2.0, 50.0), -- Factory A to Warehouse B
(1, 3, 150.0, 3.0, 70.0), -- Factory A to Warehouse C
(2, 4, 50.0, 1.0, 30.0),  -- Warehouse B to Store D
(2, 5, 80.0, 1.5, 40.0),  -- Warehouse B to Store E
(3, 6, 120.0, 2.5, 60.0), -- Warehouse C to Distribution Hub F
(6, 7, 90.0, 1.5, 50.0),  -- Distribution Hub F to Retail Center G
(5, 7, 70.0, 1.0, 40.0)   -- Store E to Retail Center G
ON CONFLICT DO NOTHING;
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

    # Execute the data insertion script
    cur.execute(insert_data_sql)
    print("BFS graph data inserted successfully.")

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
