from abc import ABC,abstractmethod

class VectorStore(ABC):
  
  @abstractmethod
  async def search(
    self,
    query_embedding:list[float],
    top_k:int    
  ):
    pass
  
  @abstractmethod
  async def add(
    self,
    embedding:list[float],
    metadata:dict,
  ):
    pass
  