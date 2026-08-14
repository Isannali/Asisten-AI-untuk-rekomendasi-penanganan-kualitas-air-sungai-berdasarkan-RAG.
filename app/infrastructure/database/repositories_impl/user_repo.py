from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.interfaces.repositories import UserRepository
from app.domain.entities.user import User as UserEntity
from app.infrastructure.database.models.user import User

class SQLAlchemyUserRepository (UserRepository):
  def __init__ (
    self,
    db:AsyncSession
    ):
    self.db=db
  
  async def get_by_id(
    self, 
    user_id
    )-> UserEntity:
    result=await self.db.execute(
      select(User).where(
        User.id==user_id
      )
    )
    user = result.scalar_one_or_none()
    
    if user is None:
      return None
    
    return UserEntity(
      id=user.id,
      created_at=user.created_at
    )
    
  async def create(
    self,
    user_id:int,
  )->UserEntity:
    user=User(
      id=user_id,
    )
    self.db.add(user)
    
    await self.db.flush()
    
    return UserEntity(
      id=user.id,
      created_at=user.created_at,
    )
