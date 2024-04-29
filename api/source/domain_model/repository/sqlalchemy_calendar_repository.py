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

    def __model_to_entity(self, calendar_model: CalendarsModel) -> Calendar:
        return Calendar(
            id=calendar_model.id,
            date=calendar_model.date,
            is_holiday=calendar_model.is_holiday
        )

    async def insert(self, calendars: List[Calendar]) -> None:
        for calendar in calendars:
            result = await self.db.execute(select(CalendarsModel).filter(CalendarsModel.date == calendar.date))
            if result.scalar() is not None:
                continue

            calendar_model = self.__toModel(calendar)
            self.db.add(calendar_model)
        await self.db.commit()

    async def fetch_holidays(self) -> List[Calendar]:
        results = await self.db.execute(select(CalendarsModel).where(CalendarsModel.is_holiday == True))

        holidays = []
        for row in results.fetchall():
            holidays.append(self.__model_to_entity(row[0]).date.strftime('%Y-%m-%d'))

        return holidays