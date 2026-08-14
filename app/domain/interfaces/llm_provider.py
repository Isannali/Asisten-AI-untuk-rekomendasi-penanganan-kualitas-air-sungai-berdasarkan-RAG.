from abc import ABC,abstractmethod

class LLMProvider(ABC):
  
  @abstractmethod
  async def generate_response(
    self,
    message:list[dict],
  )-> str:
    pass