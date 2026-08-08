from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
import ssl

class Base(DeclarativeBase):
    pass

ssl_context = ssl.create_default_context()
engine = create_async_engine(
  settings.database_url,
  connect_args={"ssl": ssl_context},
  echo=True
)

AsyncSessionLocal = async_sessionmaker(
  bind=engine,
  class_=AsyncSession,
  expire_on_commit=False,
  )

async def get_db():
  async with AsyncSessionLocal() as session:
    yield session