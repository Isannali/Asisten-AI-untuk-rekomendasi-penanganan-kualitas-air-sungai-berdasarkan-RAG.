from datetime import datetime
from sqlalchemy import DateTime, ForeignKey,Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Conversation(Base):
    __tablename__ = "conversations"
    
    id: Mapped[int] = mapped_column(
      Integer, 
      primary_key=True, 
      index=True,
      autoincrement=True
      )
    user_id: Mapped[datetime] = mapped_column(
      ForeignKey("users.id"), 
      nullable=False,
      )
    created_at: Mapped[datetime] = mapped_column(
      DateTime, 
      default=datetime.utcnow,
      )
        
