from fastapi import FastAPI,Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.presentation.api.v1.routes.chat import router as chat_router

app = FastAPI(
  title="Rag_airSungai",
  version="1.0.0"
)
app.include_router(chat_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
  
@app.get("/db-test")
async def db_test(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"database":"connected"}