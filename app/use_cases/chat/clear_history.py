from app.domain.interfaces.repositories import MessageRepository

class ClearHistory:
  def __init__(
    self,
    message_repository:MessageRepository,
    ):
    self.message_repository=message_repository
    
  async def excecute(
    self,
    conversation_id,
  ):
    await self.message_repository.delete(
      conversation_id=conversation_id
    )
    