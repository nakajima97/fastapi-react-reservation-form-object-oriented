from datetime import datetime

from source.domain_model.entity.calendar import Calendar
from source.domain_model.repository.sqlalchemy_calendar_repository import (
    SqlAlchemyCalendarRepository,
)


class FetchCalendarsByDate:
    def __init__(self, calendar_repository: SqlAlchemyCalendarRepository):
        self.calendar_repository = calendar_repository

    async def execute(self, start_date: datetime, end_date: datetime):
        return await self.calendar_repository.fetch_calendar(start_date, end_date)
