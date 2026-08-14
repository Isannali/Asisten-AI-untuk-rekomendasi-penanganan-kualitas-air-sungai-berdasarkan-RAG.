from app.domain.interfaces.llm_provider import LLMProvider
from app.infrastructure.llm.openai_client import OpenAIClient

def test_openai_client_implements_llm_provider():
  assert issubclass(
    OpenAIClient,
    LLMProvider
  )