from typing import AsyncGenerator
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.domain.interfaces.vector_store import VectorStore
from app.infrastructure.vector_store.neon_pgvector import NeonPgVector

async def get_vector_store(
  db:AsyncSession=Depends(get_db)
)-> VectorStore:
  return NeonPgVector(db)