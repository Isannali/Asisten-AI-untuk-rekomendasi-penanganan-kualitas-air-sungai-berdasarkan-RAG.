from app.domain.interfaces.vector_store import VectorStore

def test_vector_store_is_abstract():
    assert VectorStore.__abstractmethods__ == {
        "add_documents",
        "similarity_search",
    }