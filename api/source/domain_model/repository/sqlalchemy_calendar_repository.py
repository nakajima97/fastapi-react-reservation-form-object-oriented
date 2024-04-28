from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from source.models.calendars import CalendarsModel

class SqlAlchemyReservationRepository():
    def __init__(self, db: Session) -> None:
        self.db = db