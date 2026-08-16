from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.vector_store import VectorStore
from app.infrastructure.database.models.document_chunk import DocumentChunk


class NeonPgVector(VectorStore):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_documents(
        self,
        documents: list[dict[str, Any]],
    ) -> None:

        for document in documents:
            chunk = DocumentChunk(
                content=document["content"],
                embedding=document["embedding"],
                metadata=document["metadata"],
            )

            self.db.add(chunk)

        await self.db.flush()

    async def similarity_search(
        self,
        query_embedding: list[float],
        top_k: int = 5,
    ) -> list[dict[str, Any]]:

        result = await self.db.execute(
            select(DocumentChunk)
            .order_by(
                DocumentChunk.embedding.cosine_distance(
                    query_embedding
                )
            )
            .limit(top_k)
        )

        chunks = result.scalars().all()

        return [
            {
                "content": chunk.content,
                "metadata": chunk.metadata,
            }
            for chunk in chunks
        ]