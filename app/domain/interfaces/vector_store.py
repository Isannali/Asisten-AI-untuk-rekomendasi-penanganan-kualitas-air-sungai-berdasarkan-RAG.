from abc import ABC,abstractmethod
from typing import Any

class VectorStore(ABC):
  
  @abstractmethod
  async def similarity_search(
    self,
    query_embedding:list[float],
    top_k:int    
  )-> list[dict[str,Any]]:
    pass
  
  @abstractmethod
  async def add_documents(
    self,
    document:list[dict[str,Any]],
  )-> None :
    pass
  