from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.repositories import ConversationRepository
from app.domain.entities.conversation import Conversation as ConversationEntity
from app.infrastructure.database.models import Conversation

class SQLAlchemyConversationRepository(ConversationRepository):
  def __init__(
    self,
    db:AsyncSession
  ):
    self.db=db
    
  async def get_by_id(
    self,
    conversation_id:int
  )->ConversationEntity:
    result= await self.db.execute(
      select(Conversation).where(
        Conversation.id==conversation_id))
    
    conversation=result.scalar_one_or_none()
    return ConversationEntity(
      id=conversation.id,
      user_id=conversation.user_id,
      created_at=conversation.created_at
    )
    
  async def create(
    self,
    user_id:int,
  )->ConversationEntity:
    conversation=Conversation(
      user_id=user_id
    )
    self.db.add(conversation)
    await self.db.flush()
    await self.db.refresh(conversation)
    
    return ConversationEntity(
      id=conversation.id,
      user_id=conversation.user_id,
      created_at=conversation.created_at,
    )
