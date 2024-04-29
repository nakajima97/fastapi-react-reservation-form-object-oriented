from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from source.models.calendars import Calendars as CalendarsModel
from source.domain_model.entity.calendar import Calendar

class SqlAlchemyCalendarRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def __toModel(self, calendar: Calendar) -> CalendarsModel:
        return CalendarsModel(**calendar.toDict())

    async def insert(self, calendars: List[Calendar]) -> None:
        for calendar in calendars:
            calendar_model = self.__toModel(calendar)
            self.db.add(calendar_model)
        await self.db.commit()