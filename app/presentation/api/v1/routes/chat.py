from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.presentation.api.schemas.chat import ChatRequest,ChatResponse
from app.presentation.api.dependencies.chat import get_procces_chat_message

router=APIRouter(
  prefix="/chat",
  tags=["Chat"]
)

@router.post(
  "",
  response_model=ChatResponse,
)
async def send_message(
  request:ChatRequest,
  db:AsyncSession=Depends (get_db)
):
  use_case=get_procces_chat_message(db)
  try:
    (
      conversation,
      user_message,
      asistant_message,
    )= await use_case.execute(
      user_id=request.user_id,
      conversation_id=request.conversation_id,
      content=request.message,
    )
    await db.commit()
    return ChatResponse(
      conversation_id=conversation.id,
      user_message=user_message.content,
      assistant_message=asistant_message.content
    )
  except ValueError as error:
    await db.rollback()
    raise HTTPException(
      status_code=404,
      detail=str(error),
    )