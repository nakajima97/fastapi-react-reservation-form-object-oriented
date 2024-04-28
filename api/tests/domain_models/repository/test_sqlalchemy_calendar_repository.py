import pytest
import pytest_asyncio
import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from source.db import Base
from source.domain_model.repository.sqlalchemy_calendar_repository import SqlAlchemyCalendarRepository
from source.domain_model.entity.calendar import Calendar
from source.models.calendars import Calendars as CalendarModel

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

async_engine = create_async_engine(ASYNC_DB_URL, echo=False)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

@pytest_asyncio.fixture
async def async_client():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session():
    async with async_session() as session:
        yield session

@pytest.mark.asyncio
async def test_insert(async_client):
    date = datetime.date(2024, 1, 1)
    is_holiday = False
    calendar = Calendar(date=date, is_holiday=is_holiday)

    async with async_session() as session:
        sqlalchemy_calendar_repository = SqlAlchemyCalendarRepository(session)
        await sqlalchemy_calendar_repository.insert([calendar])

        # データベースからデータを取得
        result = await session.execute(select(CalendarModel).where(CalendarModel.date == date))
        inserted_calendar = result.scalars().first()

        # データが期待通りであることを確認
        assert inserted_calendar.date == date
        assert inserted_calendar.is_holiday == is_holiday