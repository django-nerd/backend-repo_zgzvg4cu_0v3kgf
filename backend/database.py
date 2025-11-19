from typing import Any, Dict, Optional
import os
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "studioledger")

_client: Optional[AsyncIOMotorClient] = None
_db: Optional[AsyncIOMotorDatabase] = None

async def get_db() -> AsyncIOMotorDatabase:
    global _client, _db
    if _db is None:
        _client = AsyncIOMotorClient(DATABASE_URL)
        _db = _client[DATABASE_NAME]
    return _db

async def create_document(collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
    db = await get_db()
    data = {**data, "_created_at": __import__('datetime').datetime.utcnow().isoformat()}
    res = await db[collection].insert_one(data)
    data["_id"] = str(res.inserted_id)
    return data

async def get_documents(collection: str, filter_dict: Dict[str, Any] | None = None, limit: int = 100):
    db = await get_db()
    cursor = db[collection].find(filter_dict or {}).limit(limit)
    out = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        out.append(doc)
    return out
