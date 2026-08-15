from app.domain.interfaces.embedding_provider import EmbeddingProvider
from openai import AsyncOpenAI
from app.config import settings
class OpenAIEmbedding(EmbeddingProvider):
  def __init__(self):
    self.client=AsyncOpenAI(
      api_key=settings.sumopod_api_key,
      base_url=settings.sumopod_base_url
      )
    self.model=settings.sumopod_embedding_model
  
  async def embed(
    self,
    text:str,
  )-> list[float]:
    text= text = text.replace('\n', ' ')   # best practice: hapus newline
    response=await self.client.embeddings.create(
      model=self.model,
      input=text
    )
    return response.data[0].embedding
  
  async def embed_batch(
    self, 
    texts:list[str],
    )-> list[list[float]]:

    response =await self.client.embeddings.create(
      model=self.model,
      input=texts,
    )
    return[
      item.embedding
      for item in response.data
    ]