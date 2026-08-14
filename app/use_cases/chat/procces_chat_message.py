from app.domain.entities.conversation import Conversation
from app.domain.entities.message import Messages
from app.domain.interfaces.repositories import(
  ConversationRepository,
  MessageRepository,
  UserRepository,
)
from app.domain.interfaces.llm_provider import LLMProvider

from typing import Optional

class ProccesChatMessage():
  def __init__(
    self,
    user_repository:UserRepository,
    conversation_repository:ConversationRepository,
    message_repository:MessageRepository,
    llm_provider:LLMProvider
  ):
    self.user_repository=user_repository
    self.conversation_repository=conversation_repository
    self.message_repository=message_repository
    self.llm_provider=llm_provider
    
  async def execute(
    self,
    user_id:int,
    content:str,
    conversation_id:Optional[int]=None ,
  ):
    #-- 1. Get or Create User--
    user=await self.user_repository.get_by_id(
      user_id=user_id
    )
    if user is None:
      user= await self.user_repository.create(
        user_id=user_id
      )
    
    #-- 2. Get or Create Conversation--
    if conversation_id is None:
      conversation = await self.conversation_repository.create(
        user_id=user_id
      )
    else:
      conversation=await self.conversation_repository.get_by_id(
        conversation_id=conversation_id
      )
      if conversation is None:
        raise ValueError("Conversation is not found")
      
    #-- 3. Save User Message--
    user_message= await self.message_repository.create(
      conversation_id=conversation.id,
      role="user",
      content=content,
    )
    
    #-- 4. get conversation history--
    history= await self.message_repository.get_history(
      conversation_id=conversation.id
    )
    
    #-- 5. convert history to llm messages --
    messages=[
      {
        "role":message.role,
        "content":message.content,
      }
      for message in history
    ]
    #--6. generate AI response--
    assistant_content=await self.llm_provider.generate_response(
      messages
    )
    
    #-- 7. Save AI Response --
    assistant_message=(
      await self.message_repository.create(
        conversation_id=conversation.id,
        role="assistant",
        content=assistant_content,
      )
    )
    return(
      conversation,
      user_message,
      assistant_message
    )