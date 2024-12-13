# bfs_query.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# BFS query
bfs_query_sql = """
WITH RECURSIVE bfs AS (
    -- Start with the initial node (Factory A)
    SELECT
        r.from_location_id,
        r.to_location_id,
        l.location_name AS from_name,
        (SELECT location_name FROM locations WHERE location_id = r.to_location_id) AS to_name,
        1 AS level
    FROM routes r
    JOIN locations l ON r.from_location_id = l.location_id
    WHERE r.from_location_id = 1 -- Starting from Factory A (ID 1)

    UNION ALL

    -- Traverse to the next level
    SELECT
        r.from_location_id,
        r.to_location_id,
        l.location_name AS from_name,
        (SELECT location_name FROM locations WHERE location_id = r.to_location_id) AS to_name,
        bfs.level + 1 AS level
    FROM routes r
    JOIN bfs ON bfs.to_location_id = r.from_location_id
    JOIN locations l ON r.from_location_id = l.location_id
)
SELECT * FROM bfs
ORDER BY level, from_name, to_name;
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

    # Execute the BFS query
    print("\nBFS Traversal Results:")
    cur.execute(bfs_query_sql)
    results = cur.fetchall()

    # Print the results
    for row in results:
        print(f"Level: {row[4]}, From: {row[2]}, To: {row[3]}")

    # Close the cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
