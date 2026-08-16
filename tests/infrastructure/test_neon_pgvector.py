from unittest.mock import AsyncMock, MagicMock

import pytest

from app.infrastructure.vector_store.neon_pgvector import NeonPgVector


@pytest.mark.asyncio
async def test_add_documents():
    db = MagicMock()
    db.flush = AsyncMock()

    vector_store = NeonPgVector(db)

    documents = [
        {
            "content": "Kualitas air sungai",
            "embedding": [0.1, 0.2, 0.3],
            "metadata": {"source": "test.pdf"},
        }
    ]

    await vector_store.add_documents(documents)

    db.add.assert_called_once()
    db.flush.assert_awaited_once()