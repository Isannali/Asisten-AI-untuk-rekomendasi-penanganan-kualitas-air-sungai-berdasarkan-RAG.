from app.domain.interfaces.repositories import (
    UserRepository,
    ConversationRepository,
    MessageRepository,
)

from app.infrastructure.database.repositories_impl.user_repo import (
    SQLAlchemyUserRepository,
)

from app.infrastructure.database.repositories_impl.conversation_repo import (
    SQLAlchemyConversationRepository,
)

from app.infrastructure.database.repositories_impl.message_repo import (
    SQLAlchemyMessageRepository,
)


def test_user_repository_implements_interface():

    assert issubclass(
        SQLAlchemyUserRepository,
        UserRepository,
    )


def test_conversation_repository_implements_interface():

    assert issubclass(
        SQLAlchemyConversationRepository,
        ConversationRepository,
    )


def test_message_repository_implements_interface():

    assert issubclass(
        SQLAlchemyMessageRepository,
        MessageRepository,
    )