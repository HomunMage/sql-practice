# create.py

import asyncio
from ..model.db import init_db, get_pool, close_db

async def main():
    # Initialize the database connection
    pool = await init_db(run_migrations=True)

    # Touch the database (simple query to confirm connection)
    async with pool.acquire() as conn:
        result = await conn.fetchval("SELECT version();")
        print(f"📦 PostgreSQL version: {result}")

    # Close the database connection pool
    await close_db()

if __name__ == "__main__":
    asyncio.run(main())
