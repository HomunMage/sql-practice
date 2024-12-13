# top5.py
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

    # Query to get the top 5 most borrowed books
    cur.execute("""
        SELECT b.title, COUNT(bh.borrow_id) AS borrow_count
        FROM BorrowingHistory bh
        JOIN Books b ON bh.book_id = b.book_id
        GROUP BY b.title
        ORDER BY borrow_count DESC
        LIMIT 5;
    """)
    top_books = cur.fetchall()
    print("Top 5 Most Borrowed Books:")
    for book in top_books:
        print(f"Book Title: {book[0]}, Borrow Count: {book[1]}")

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
