# src/model/library_crud.py

"""
CRUD operations for the Library Management System.
Tables: authors, books, members, borrowing_history
"""

from datetime import date
from .db import get_pool


# -------------------- AUTHORS --------------------

async def create_author(name: str, birth_date: date = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            INSERT INTO authors (name, birth_date)
            VALUES ($1, $2)
            RETURNING *;
            """,
            name, birth_date
        )

async def get_author(author_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow("SELECT * FROM authors WHERE author_id = $1;", author_id)

async def get_all_authors():
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT * FROM authors ORDER BY name;")

async def update_author(author_id: int, name: str = None, birth_date: date = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            UPDATE authors
            SET name = COALESCE($2, name),
                birth_date = COALESCE($3, birth_date)
            WHERE author_id = $1
            RETURNING *;
            """,
            author_id, name, birth_date
        )

async def delete_author(author_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("DELETE FROM authors WHERE author_id = $1;", author_id)
        return True


# -------------------- BOOKS --------------------

async def create_book(title: str, publisher: str = None, publication_year: int = None, isbn: str = None, author_id: int = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            INSERT INTO books (title, publisher, publication_year, isbn, author_id)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING *;
            """,
            title, publisher, publication_year, isbn, author_id
        )

async def get_book(book_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            SELECT b.*, a.name AS author_name
            FROM books b
            LEFT JOIN authors a ON b.author_id = a.author_id
            WHERE b.book_id = $1;
            """,
            book_id
        )

async def get_all_books():
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetch(
            """
            SELECT b.*, a.name AS author_name
            FROM books b
            LEFT JOIN authors a ON b.author_id = a.author_id
            ORDER BY b.title;
            """
        )

async def update_book(book_id: int, title: str = None, publisher: str = None, publication_year: int = None, isbn: str = None, author_id: int = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            UPDATE books
            SET title = COALESCE($2, title),
                publisher = COALESCE($3, publisher),
                publication_year = COALESCE($4, publication_year),
                isbn = COALESCE($5, isbn),
                author_id = COALESCE($6, author_id)
            WHERE book_id = $1
            RETURNING *;
            """,
            book_id, title, publisher, publication_year, isbn, author_id
        )

async def delete_book(book_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("DELETE FROM books WHERE book_id = $1;", book_id)
        return True


# -------------------- MEMBERS --------------------

async def create_member(name: str, membership_date: date = None, email: str = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            INSERT INTO members (name, membership_date, email)
            VALUES ($1, $2, $3)
            RETURNING *;
            """,
            name, membership_date, email
        )

async def get_member(member_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow("SELECT * FROM members WHERE member_id = $1;", member_id)

async def get_all_members():
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT * FROM members ORDER BY name;")

async def update_member(member_id: int, name: str = None, membership_date: date = None, email: str = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            UPDATE members
            SET name = COALESCE($2, name),
                membership_date = COALESCE($3, membership_date),
                email = COALESCE($4, email)
            WHERE member_id = $1
            RETURNING *;
            """,
            member_id, name, membership_date, email
        )

async def delete_member(member_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("DELETE FROM members WHERE member_id = $1;", member_id)
        return True


# -------------------- BORROWING HISTORY --------------------

async def create_borrow_record(book_id: int, member_id: int, borrow_date: date, return_date: date = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            INSERT INTO borrowing_history (book_id, member_id, borrow_date, return_date)
            VALUES ($1, $2, $3, $4)
            RETURNING *;
            """,
            book_id, member_id, borrow_date, return_date
        )

async def get_borrow_record(borrow_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            SELECT bh.*, b.title AS book_title, m.name AS member_name
            FROM borrowing_history bh
            JOIN books b ON bh.book_id = b.book_id
            JOIN members m ON bh.member_id = m.member_id
            WHERE bh.borrow_id = $1;
            """,
            borrow_id
        )

async def get_all_borrow_records():
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetch(
            """
            SELECT bh.*, b.title AS book_title, m.name AS member_name
            FROM borrowing_history bh
            JOIN books b ON bh.book_id = b.book_id
            JOIN members m ON bh.member_id = m.member_id
            ORDER BY bh.borrow_date DESC;
            """
        )

async def update_borrow_record(borrow_id: int, return_date: date = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            """
            UPDATE borrowing_history
            SET return_date = COALESCE($2, return_date)
            WHERE borrow_id = $1
            RETURNING *;
            """,
            borrow_id, return_date
        )

async def delete_borrow_record(borrow_id: int):
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("DELETE FROM borrowing_history WHERE borrow_id = $1;", borrow_id)
        return True
