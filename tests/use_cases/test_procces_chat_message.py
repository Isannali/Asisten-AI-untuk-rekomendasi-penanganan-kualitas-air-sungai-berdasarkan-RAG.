import pytest
from datetime import datetime
from app.use_cases.chat.procces_chat_message import (
    ProccesChatMessage,
)
from app.domain.entities.conversation import Conversation
from app.domain.entities.message import Messages
from app.domain.entities.user import User


class FakeUserRepository:

    async def get_by_id(self, user_id):
        return User(
            id=user_id,
            created_at=datetime.utcnow
        )

    async def create(self, user_id):
        return User(
            id=user_id
        )


class FakeConversationRepository:

    async def create(self, user_id):
        return Conversation(
            id=1,
            user_id=user_id,
            created_at=datetime.utcnow,
        )

    async def get_by_id(self, conversation_id):
        return Conversation(
            id=conversation_id,
            user_id=1,
            created_at=datetime.utcnow,
        )


class FakeMessageRepository:

    def __init__(self):
        self.messages = []

    async def create(
        self,
        conversation_id,
        role,
        content,
    ):
        message = Messages(
            id=len(self.messages) + 1,
            conversation_id=conversation_id,
            role=role,
            content=content,
            created_at=datetime.utcnow,
        )

        self.messages.append(message)

        return message

    async def get_history(self, conversation_id):
        return self.messages


class FakeLLMProvider:

    async def generate_response(self, messages):

        return "TSS adalah Total Suspended Solids."


@pytest.mark.asyncio
async def test_process_chat_message():

    user_repository = FakeUserRepository()

    conversation_repository = (
        FakeConversationRepository()
    )

    message_repository = (
        FakeMessageRepository()
    )

    llm_provider = FakeLLMProvider()

    use_case = ProccesChatMessage(
        user_repository=user_repository,
        conversation_repository=conversation_repository,
        message_repository=message_repository,
        llm_provider=llm_provider,
    )

    conversation, user_message, assistant_message = (
        await use_case.execute(
            user_id=1,
            content="Apa itu TSS?",
            conversation_id=None,
        )
    )

    assert conversation.id == 1

    assert user_message.role == "user"
    assert user_message.content == "Apa itu TSS?"

    assert assistant_message.role == "assistant"
    assert (
        assistant_message.content
        == "TSS adalah Total Suspended Solids."
    )
    
@pytest.mark.asyncio
async def test_process_chat_message_existing_conversation():

    user_repository = FakeUserRepository()

    conversation_repository = (
        FakeConversationRepository()
    )

    message_repository = (
        FakeMessageRepository()
    )

    llm_provider = FakeLLMProvider()

    use_case = ProccesChatMessage(
        user_repository=user_repository,
        conversation_repository=conversation_repository,
        message_repository=message_repository,
        llm_provider=llm_provider,
    )

    (
        conversation,
        user_message,
        assistant_message,
    ) = await use_case.execute(
        user_id=1,
        content="Bagaimana cara mengurangi TSS?",
        conversation_id=10,
    )

    assert conversation.id == 10

    assert user_message.conversation_id == 10

    assert user_message.role == "user"

    assert (
        user_message.content
        == "Bagaimana cara mengurangi TSS?"
    )

    assert assistant_message.conversation_id == 10

    assert assistant_message.role == "assistant"
    
@pytest.mark.asyncio
async def test_process_chat_message_conversation_not_found():

    user_repository = FakeUserRepository()

    conversation_repository = (
        FakeConversationRepository()
    )

    message_repository = (
        FakeMessageRepository()
    )

    llm_provider = FakeLLMProvider()

    # Buat repository yang menganggap
    # conversation_id tertentu tidak ditemukan
    async def get_by_id(conversation_id):
        return None

    conversation_repository.get_by_id = get_by_id

    use_case = ProccesChatMessage(
        user_repository=user_repository,
        conversation_repository=conversation_repository,
        message_repository=message_repository,
        llm_provider=llm_provider,
    )

    with pytest.raises(
        ValueError,
        match="Conversation is not found",
    ):

        await use_case.execute(
            user_id=1,
            content="Apa itu TSS?",
            conversation_id=999,
        )