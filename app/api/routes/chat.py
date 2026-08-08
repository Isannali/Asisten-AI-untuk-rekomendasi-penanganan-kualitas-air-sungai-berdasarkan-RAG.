from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.chat import (
  ChatRequest,
  ChatResponse,
)
from app.services.chat_services import ChatService

router=APIRouter(
  prefix="/chat",
  tags=["Chat"]
)
chat_service=ChatService()

@router.post("",response_model=ChatResponse)
async def send_message(
  request:ChatRequest,
  db:AsyncSession=Depends(get_db),
):
  try:
    conversation,message=(
      await chat_service.send_message(
        db=db,
        user_id=request.user_id,
        conversation_id=request.conversation_id,
        content=request.message,
      )
    )
  except ValueError as error:
    raise HTTPException(
      status_code=404,
      detail=str(error),
    )
  return ChatResponse(
    conversation_id=conversation.id,
    message_id=message.id,
    role=message.role,
    content=message.content,
  )

@router.get("/{conversation_id}")
async def get_chat_history(
  conversation_id:int,
  db:AsyncSession=Depends(get_db),
):
  messages=await chat_service.get_history(
    db,
    conversation_id,
  )
  return{
    "conversation_id": conversation_id,
    "messages":[{
      "id":message.id,
      "role":message.role,
      "content": message.content,
      "created_at":message.created_at,
    }
    for message in messages
    ],
  }