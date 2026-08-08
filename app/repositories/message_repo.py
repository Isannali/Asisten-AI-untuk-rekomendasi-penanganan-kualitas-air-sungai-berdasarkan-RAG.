from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.message import Message


class MessageRepository:

    async def create(
        self,
        db: AsyncSession,
        conversation_id: int,
        role: str,
        content: str,
    ) :

        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
        )

        db.add(message)

        await db.flush()

        return message

    async def get_history(
        self,
        db: AsyncSession,
        conversation_id: int,
    ) :

        result = await db.execute(
            select(Message)
            .where(
                Message.conversation_id == conversation_id
            )
            .order_by(Message.created_at.asc())
        )

        return list(result.scalars().all())