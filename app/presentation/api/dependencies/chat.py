from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.repositories_impl.user_repo import SQLAlchemyUserRepository
from app.infrastructure.database.repositories_impl.conversation_repo import SQLAlchemyConversationRepository
from app.infrastructure.database.repositories_impl.message_repo import SQLAlchemyMessageRepository

from app.infrastructure.llm.openai_client import OpenAIClient

from app.use_cases.chat.procces_chat_message import ProccesChatMessage

def get_procces_chat_message(
  db:AsyncSession
)-> ProccesChatMessage:
  user_repository=SQLAlchemyUserRepository(db)
  conversation_repository=SQLAlchemyConversationRepository(db)
  message_repository=SQLAlchemyMessageRepository(db)
  llm_provider=OpenAIClient()
  
  return ProccesChatMessage(
    user_repository=user_repository,
    conversation_repository=conversation_repository,
    message_repository=message_repository,
    llm_provider=llm_provider,
  )
  