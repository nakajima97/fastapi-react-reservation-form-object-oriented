from datetime import datetime
from datetime import timedelta

from source.domain_model.entity.calendar import Calendar
from source.domain_model.repository.sqlalchemy_calendar_repository import (
    SqlAlchemyCalendarRepository,
)


class StoreCalendarsByDate:
    def __init__(self, calendar_repository: SqlAlchemyCalendarRepository):
        self.calendar_repository = calendar_repository

    async def execute(self, start_date: datetime, end_date: datetime):
        calendars = []
        for date in date_range(start_date, end_date):
            calendar = Calendar(date=date, is_holiday=True)
            calendars.append(calendar)

        await self.calendar_repository.insert(calendars)


def date_range(_start, _end):
    for n in range((_end - _start).days + 1):
        yield _start + timedelta(n)
