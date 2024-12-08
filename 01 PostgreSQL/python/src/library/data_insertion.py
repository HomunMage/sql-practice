# data_insertion.py
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

    # Step 1: Insert authors first
    cur.execute("""
        INSERT INTO Authors (name, birth_date) VALUES
        ('J.K. Rowling', '1965-07-31'),
        ('George Orwell', '1903-06-25'),
        ('J.R.R. Tolkien', '1892-01-03')
        ON CONFLICT (name) DO NOTHING;  -- Prevent inserting duplicates
    """)

    # Step 2: Insert books with author_id correctly linked
    cur.execute("""
        INSERT INTO Books (title, publisher, publication_year, isbn, author_id) VALUES
        ('Harry Potter and the Sorcerer''s Stone', 'Bloomsbury', 1997, '978-0747532699', 1),
        ('1984', 'Secker & Warburg', 1949, '978-0451524935', 2),
        ('The Hobbit', 'George Allen & Unwin', 1937, '978-0618968633', 3)
        ON CONFLICT (isbn) DO NOTHING;  -- Prevent inserting duplicates
    """)

    # Insert some members
    cur.execute("""
        INSERT INTO Members (name, membership_date, email) VALUES
        ('Alice Johnson', '2020-05-10', 'alice@example.com'),
        ('Bob Smith', '2022-02-15', 'bob@example.com')
        ON CONFLICT (email) DO NOTHING;  -- Prevent inserting duplicates
    """)

    # Insert some borrowing history
    cur.execute("""
        INSERT INTO BorrowingHistory (book_id, member_id, borrow_date, return_date) VALUES
        (1, 1, '2023-01-15', '2023-02-15'),
        (2, 2, '2023-04-20', NULL)
        ON CONFLICT DO NOTHING;  -- Prevent inserting duplicates
    """)

    # Commit the transaction to ensure data is saved
    conn.commit()
    print("Data inserted successfully.")

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
