from abc import ABC,abstractmethod

from app.domain.entities.conversation import Conversation
from app.domain.entities.message import Messages
from app.domain.entities.user import User

class UserRepository(ABC):
  
  @abstractmethod
  async def get_by_id(
    self,
    user_id:int,
  ) -> User:
    pass
  
  @abstractmethod
  async def create(
    self,
    user_id:int,
  )-> User:
    pass
  
class ConversationRepository(ABC):
  
  @abstractmethod
  async def get_by_id (
    self,
    conversation_id:int
  )->Conversation:
    pass
  
  @abstractmethod
  async def create(
    self,
    user_id:int,
  )->Conversation:
    pass
  
class MessageRepository(ABC):
  
  @abstractmethod
  async def get_history(
    self,
    conversation_id:int,
  )-> list[Messages]:
    pass
  
  @abstractmethod
  async def create(
    self,
    conversation_id:int,
    role:str,
    content:str
  )-> Messages:
    pass
  
  @abstractmethod
  async def delete(
    self,
    conversation_id:int,
  )-> None:
    pass