import pytest

from app.infrastructure.embedding.openai_embedding import OpenAIEmbedding


@pytest.mark.asyncio
async def test_embed():
    provider = OpenAIEmbedding()

    embedding = await provider.embed(
        "Kualitas air sungai"
    )

    assert isinstance(embedding, list)
    assert len(embedding) > 0
    assert all(isinstance(value, float) for value in embedding)
    
import pytest

from app.infrastructure.embedding.openai_embedding import OpenAIEmbedding


@pytest.mark.asyncio
async def test_embed_batch():
    provider = OpenAIEmbedding()

    texts = [
        "Kualitas air sungai",
        "Parameter pH air",
        "Baku mutu air sungai",
    ]

    embeddings = await provider.embed_batch(texts)

    assert isinstance(embeddings, list)
    assert len(embeddings) == len(texts)

    for embedding in embeddings:
        assert isinstance(embedding, list)
        assert len(embedding) > 0
        assert all(isinstance(value, float) for value in embedding)

@pytest.mark.asyncio
async def test_embedding_dimension_consistency():
    provider = OpenAIEmbedding()

    embeddings = await provider.embed_batch(
        [
            "Kualitas air sungai",
            "Parameter pH air",
            "Baku mutu air sungai",
        ]
    )

    dimensions = {len(embedding) for embedding in embeddings}

    assert len(dimensions) == 1