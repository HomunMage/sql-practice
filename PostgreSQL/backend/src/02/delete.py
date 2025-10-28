# delete.py

import asyncio
from ..model.db import get_pool

async def clean_library():
    """
    Drop all library-related tables safely if they exist.
    """
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.transaction():
            print("⚙️ Dropping existing library tables (if they exist)...")
            
            # Drop tables in correct dependency order
            await conn.execute("DROP TABLE IF EXISTS borrowing_history CASCADE;")
            await conn.execute("DROP TABLE IF EXISTS books CASCADE;")
            await conn.execute("DROP TABLE IF EXISTS members CASCADE;")
            await conn.execute("DROP TABLE IF EXISTS authors CASCADE;")
            
            print("✅ Library tables deleted successfully.")

if __name__ == "__main__":
    asyncio.run(clean_library())
