import pytest

from app.domain.interfaces.vector_store import VectorStore
from app.infrastructure.vector_store.neon_pgvector import NeonPgVector
from app.presentation.dependencies.vector_store import get_vector_store

@pytest.mark.asyncio
async def test_get_vector_store():
  db=None
  vector_store= await get_vector_store(db)
  
  assert isinstance(vector_store,NeonPgVector)
  assert isinstance(vector_store,VectorStore)