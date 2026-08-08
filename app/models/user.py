from datetime import datetime
from sqlalchemy import  DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(
      Integer, 
      primary_key=True, 
      index=True
      )
    created_at: Mapped[datetime] = mapped_column(
      DateTime, 
      default=datetime.utcnow
      )
    # updated_at: Mapped[datetime] = mapped_column(
      # DateTime, 
      # default=datetime.utcnow,
      # onupdate=datetime.utcnow
      # )
    