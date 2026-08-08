from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User

class UserRepository:
  async def get_by_id(
    self,
    db:AsyncSession,
    user_id:int,):
    return await db.get(User,user_id)
  
  async def create(self,db:AsyncSession,user_id:int):
    user=User(id=user_id)
    db.add(user)
    await db.flush()
    return user
  
