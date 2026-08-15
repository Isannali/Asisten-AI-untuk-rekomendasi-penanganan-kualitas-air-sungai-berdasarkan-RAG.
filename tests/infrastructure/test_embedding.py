from app.infrastructure.embedding.openai_embedding import OpenAIEmbedding

def test_embedding_provider() :
  provider = OpenAIEmbedding()
  
  assert provider.client is not None
  assert provider.model
