import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_signup_and_get_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/signup", json={
            "name": "Alice",
            "email": "alice@example.com",
            "password": "secret",
            "allergies": ["nuts"]
        })
        assert response.status_code == 200

        res = await ac.get("/users/alice@example.com")
        assert res.status_code == 200
