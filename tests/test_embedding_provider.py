from app.domain.interfaces.embedding_provider import EmbeddingProvider

def test_embedding_provider_is_abstract():
  assert EmbeddingProvider.__abstractmethods__=={
    "embed",
    "embed_batch",
  }