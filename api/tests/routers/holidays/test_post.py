import pytest
import pytest_asyncio
import starlette.status

from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import datetime

from source.db import get_db, Base
from source.main import app
import source.models.calendars as calendars_model
import source.models.reservations as reservations_model

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

async_engine = create_async_engine(ASYNC_DB_URL, echo=False)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)


@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async def get_test_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_create_holidays(async_client):
    base_json = {"holidays": ["2024-05-10", "2024-05-11"]}
    response = await async_client.post("/holidays", json=base_json)
    assert response.status_code == starlette.status.HTTP_200_OK
    response_object = response.json()
    assert response_object["holidays"] == base_json["holidays"]
