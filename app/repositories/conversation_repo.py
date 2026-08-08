from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.conversation import Conversation

class ConversationRepository:
  async def get_by_id(
    self,
    db:AsyncSession,
    conversation_id:int,):
    result= await db.execute(select(Conversation).where(Conversation.id== conversation_id))
    return result.scalar_one_or_none()
  
  async def create(self,db:AsyncSession,user_id:int,):
    conversation=Conversation(user_id=user_id)
    db.add(conversation)
    await db.flush()
    return conversation