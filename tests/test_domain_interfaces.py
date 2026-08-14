from app.domain.interfaces.repositories import (
    UserRepository,
    ConversationRepository,
    MessageRepository,
)

from app.domain.interfaces.llm_provider import (
    LLMProvider,
)

from app.domain.interfaces.vector_store import (
    VectorStore,
)


def test_repository_interfaces_exist():

    assert UserRepository is not None
    assert ConversationRepository is not None
    assert MessageRepository is not None


def test_llm_interface_exists():

    assert LLMProvider is not None


def test_vector_store_interface_exists():

    assert VectorStore is not None