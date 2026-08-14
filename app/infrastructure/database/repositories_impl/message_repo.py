from sqlalchemy import select,delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.repositories import MessageRepository
from app.domain.entities.message import Messages as MessageEntity
from app.infrastructure.database.models.message import Message

class SQLAlchemyMessageRepository (MessageRepository):
  def __init__ (
    self,
    db:AsyncSession
    ):
    self.db=db
  
  async def get_history(
    self, 
    conversation_id:int
    )-> list[MessageEntity]:
    result = await self.db.execute(
        select(Message)
        .where(
            Message.conversation_id == conversation_id
        )
        .order_by(Message.created_at.asc())
    )
    messages=result.scalars().all()
    return [
      MessageEntity(
        id=message.id,
        conversation_id=message.conversation_id,
        role= message.role,
        content=message.content,
        created_at=message.created_at,
      )
      for message in messages
      ]   
    
  async def create(
    self,
    conversation_id:int,
    role:str,
    content:str,
  )-> MessageEntity:
    message=Message(
      conversation_id=conversation_id,
      role=role,
      content=content,
    )
    self.db.add(message)
    
    await self.db.flush()
    
    return MessageEntity(
      id=message.id,
      conversation_id=message.conversation_id,
      role=message.role,
      content=message.content,
      created_at=message.created_at
    )
  
  async def delete(
    self,
    conversation_id:int,
  ):
    await self.db.execute(
      delete(Message).where(
        Message.conversation_id==conversation_id
      )
    )
    await self.db.flush()
