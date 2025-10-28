# src/main.py

import asyncio
from datetime import date
from ..model.db import init_db, close_db
from ..model import library_crud as crud


async def main():
    # 1️⃣ Initialize database and run migrations
    await init_db(run_migrations=True)

    print("\n=== Inserting sample data ===")

    # 2️⃣ Create Authors
    authors = [
        await crud.create_author("George Orwell", date(1903, 6, 25)),
        await crud.create_author("Harper Lee", date(1926, 4, 28)),
        await crud.create_author("J.K. Rowling", date(1965, 7, 31)),
    ]

    print(f"Inserted {len(authors)} authors.\n")

    # 3️⃣ Create Books
    books = [
        await crud.create_book("1984", "Secker & Warburg", 1949, "9780451524935", authors[0]["author_id"]),
        await crud.create_book("Animal Farm", "Secker & Warburg", 1945, "9780451526342", authors[0]["author_id"]),
        await crud.create_book("To Kill a Mockingbird", "J.B. Lippincott & Co.", 1960, "9780061120084", authors[1]["author_id"]),
        await crud.create_book("Harry Potter and the Philosopher's Stone", "Bloomsbury", 1997, "9780747532699", authors[2]["author_id"]),
    ]

    print(f"Inserted {len(books)} books.\n")

    # 4️⃣ Create Members
    members = [
        await crud.create_member("Alice Smith", date(2023, 1, 10), "alice@example.com"),
        await crud.create_member("Bob Johnson", date(2023, 2, 5), "bob@example.com"),
    ]

    print(f"Inserted {len(members)} members.\n")

    # 5️⃣ Create Borrowing Records
    borrows = [
        await crud.create_borrow_record(books[0]["book_id"], members[0]["member_id"], date(2025, 10, 1)),
        await crud.create_borrow_record(books[2]["book_id"], members[1]["member_id"], date(2025, 10, 5), date(2025, 10, 20)),
    ]

    print(f"Inserted {len(borrows)} borrowing records.\n")

    # 6️⃣ Query All
    print("\n=== All Authors ===")
    for author in await crud.get_all_authors():
        print(dict(author))

    print("\n=== All Books ===")
    for book in await crud.get_all_books():
        print(dict(book))

    print("\n=== All Members ===")
    for member in await crud.get_all_members():
        print(dict(member))

    print("\n=== All Borrow Records ===")
    for record in await crud.get_all_borrow_records():
        print(dict(record))

    # 7️⃣ Example Query by ID
    george = await crud.get_author(authors[0]["author_id"])
    print(f"\nAuthor Lookup -> {george['name']} (born {george['birth_date']})")

    # 8️⃣ Example Update
    updated_member = await crud.update_member(members[0]["member_id"], email="alice.smith@newmail.com")
    print(f"\nUpdated Member -> {dict(updated_member)}")

    # 9️⃣ Example Delete
    await crud.delete_book(books[1]["book_id"])
    print("\nDeleted 'Animal Farm' successfully.")

    # 10️⃣ Clean up
    await close_db()


if __name__ == "__main__":
    asyncio.run(main())
