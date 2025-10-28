# data_insertion.py

import asyncio
from ..model.db import get_pool

async def insert_sample_data():
    """
    Insert initial sample data into the database tables.
    Avoids duplicates using ON CONFLICT clauses.
    """
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.transaction():
            # Insert authors
            await conn.execute("""
                INSERT INTO authors (name, birth_date) VALUES
                ('J.K. Rowling', '1965-07-31'),
                ('George Orwell', '1903-06-25'),
                ('J.R.R. Tolkien', '1892-01-03')
                ON CONFLICT (name) DO NOTHING;
            """)

            # Insert books linked to authors
            await conn.execute("""
                INSERT INTO books (title, publisher, publication_year, isbn, author_id)
                VALUES
                ('Harry Potter and the Sorcerer''s Stone', 'Bloomsbury', 1997, '978-0747532699',
                    (SELECT author_id FROM authors WHERE name = 'J.K. Rowling')),
                ('1984', 'Secker & Warburg', 1949, '978-0451524935',
                    (SELECT author_id FROM authors WHERE name = 'George Orwell')),
                ('The Hobbit', 'George Allen & Unwin', 1937, '978-0618968633',
                    (SELECT author_id FROM authors WHERE name = 'J.R.R. Tolkien'))
                ON CONFLICT (isbn) DO NOTHING;
            """)

            # Insert members
            await conn.execute("""
                INSERT INTO members (name, membership_date, email) VALUES
                ('Alice Johnson', '2020-05-10', 'alice@example.com'),
                ('Bob Smith', '2022-02-15', 'bob@example.com')
                ON CONFLICT (email) DO NOTHING;
            """)

            # Insert borrowing history
            await conn.execute("""
                INSERT INTO borrowing_history (book_id, member_id, borrow_date, return_date) VALUES
                ((SELECT book_id FROM books WHERE title = 'Harry Potter and the Sorcerer''s Stone'),
                 (SELECT member_id FROM members WHERE email = 'alice@example.com'),
                 '2023-01-15', '2023-02-15'),
                ((SELECT book_id FROM books WHERE title = '1984'),
                 (SELECT member_id FROM members WHERE email = 'bob@example.com'),
                 '2023-04-20', NULL)
                ON CONFLICT DO NOTHING;
            """)

            print("✅ Sample data inserted successfully.")

if __name__ == "__main__":
    asyncio.run(insert_sample_data())
