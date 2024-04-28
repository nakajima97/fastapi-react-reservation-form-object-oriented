from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from source.models.calendars import CalendarsModel

class SqlAlchemyReservationRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def fetch_holidays(self):
        result = db.execute(select(CalendarsModel.date).where(CalendarsModel.is_holiday == True))
        result_all = result.all()

        # 件数が0件の場合は空リストを返す
        if len(result_all) == 0:
            return []

        return [raw[0] for raw in result_all]