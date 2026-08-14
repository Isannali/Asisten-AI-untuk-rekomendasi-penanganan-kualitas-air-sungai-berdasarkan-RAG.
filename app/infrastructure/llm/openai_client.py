from openai import AsyncOpenAI

from app.config import settings
from app.domain.interfaces.llm_provider import LLMProvider

class OpenAIClient(LLMProvider):
  def __init__(self):
    self.client=AsyncOpenAI(
      api_key=settings.sumopod_api_key,
      base_url=settings.sumopod_base_url,
    )
  
  async def generate_response(
    self, 
    messages:list[dict],
    )-> str :
    response=await self.client.chat.completions.create(
      model=settings.sumopod_model_llm,
      messages=messages
    )
    return response.choices[0].message.content