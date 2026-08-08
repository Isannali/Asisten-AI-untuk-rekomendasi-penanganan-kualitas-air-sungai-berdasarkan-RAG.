from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.conversation_repo import ConversationRepository
from app.repositories.message_repo import MessageRepository
from app.repositories.user_repo import UserRepository

class ChatService:
  def __init__(self):
    self.user_repo=UserRepository()
    self.conversation_repo=ConversationRepository()
    self.message_repo=MessageRepository()
  
  async def send_message(
    self,
    db:AsyncSession,
    user_id:int,
    conversation_id:int,
    content:str,
  ):
    user=await self.user_repo.get_by_id(
      db,
      user_id,
    )
    if user is None:
      user=await self.user_repo.create(db,user_id)
      user.id=user_id
    
    if conversation_id is None:
      conversation=(
        await self.conversation_repo.create(
          db,
          user_id,
        )
      )
    
    else:
      conversation=await self.conversation_repo.get_by_id(
          db,
          conversation_id,
          )
      
      if conversation is None:
        raise ValueError(
          "Conversation is not found"
        )
    
    message=await self.message_repo.create(
      db=db,
      conversation_id=conversation.id,
      role="user",
      content= content
    )
    await db.commit()
    return conversation,message
  
  async def get_history(
    self,
    db:AsyncSession,
    conversation_id:int,
  ):
    return await self.message_repo.get_history(
      db,
      conversation_id,
    )