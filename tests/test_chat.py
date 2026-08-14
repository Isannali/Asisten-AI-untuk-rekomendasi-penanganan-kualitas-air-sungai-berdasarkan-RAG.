import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_send_message():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/chat",
            json={
                "user_id": 1,
                "conversation_id": None,
                "message": "Apa itu TSS?"
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert "conversation_id" in data
    assert "user_message" in data
    assert "assistant_message" in data