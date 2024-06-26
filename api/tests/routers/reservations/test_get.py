import pytest
import pytest_asyncio
import starlette.status

from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import datetime

from source.db import get_db, Base
from source.main import app
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
async def test_get_reservations_no_data(async_client):
    response = await async_client.get("/reservations")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_object = response.json()
    assert response_object["reservations"] == []


@pytest.mark.asyncio
async def test_get_reservations_with_data(async_client):
    base_json = {
        "date": "2024-01-01",
        "name": "テスト　ヨヤク",
        "email_address": "example@example.com",
        "phone_number": "123-456-7890",
    }

    async with async_session() as session:
        reservation = reservations_model.Reservations(
            date=datetime.datetime.strptime(base_json["date"], "%Y-%m-%d"),
            name=base_json["name"],
            email_address=base_json["email_address"],
            phone_number=base_json["phone_number"],
        )
        session.add(reservation)
        await session.commit()

    response = await async_client.get("/reservations")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_object = response.json()
    assert response_object["reservations"][0]["date"] == base_json["date"]
    assert response_object["reservations"][0]["name"] == base_json["name"]
    assert (
        response_object["reservations"][0]["email_address"]
        == base_json["email_address"]
    )
    assert (
        response_object["reservations"][0]["phone_number"] == base_json["phone_number"]
    )
