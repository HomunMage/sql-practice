# top5.py

import asyncio
from ..model.db import get_pool

async def get_top5_books():
    """
    Fetch and display the top 5 most borrowed books.
    """
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch("""
            SELECT b.title, COUNT(bh.borrow_id) AS borrow_count
            FROM borrowing_history bh
            JOIN books b ON bh.book_id = b.book_id
            GROUP BY b.title
            ORDER BY borrow_count DESC
            LIMIT 5;
        """)

        print("📚 Top 5 Most Borrowed Books:")
        if not rows:
            print("No borrowing records found.")
            return

        for row in rows:
            print(f"Book Title: {row['title']}, Borrow Count: {row['borrow_count']}")

if __name__ == "__main__":
    asyncio.run(get_top5_books())
