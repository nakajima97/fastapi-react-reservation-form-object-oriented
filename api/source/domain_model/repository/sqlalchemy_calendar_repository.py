from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from source.models.calendars import CalendarsModel
from source.domain_model.entity.calendar import Calendar

class SqlAlchemyReservationRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def __toModel(self, calendar: Calendar) -> CalendarsModel:
    return CalendarsModel(**calendar.toDict())

    async def insert(self, calendars: List[CalendarsModel]) -> None:
        for calendar in calendars:
            calendar_model = self.__toModel(calendar)

            if self.db.execute(select(CalendarsModel).where(CalendarsModel.date == calendar_model.date)).first() is None:
                self.db.add(calendar_model)
                await self.db.commit()
                await self.db.refresh(calendar_model)