from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from source.db import get_db
from source.schemas.holidays import Holidays
from source.domain_model.repository.sqlalchemy_calendar_repository import SqlAlchemyCalendarRepository
from source.domain_model.entity.calendar import Calendar
from source.domain_model.usecase.holiday.store_holidays import StoreHolidays
from source.domain_model.usecase.holiday.fetch_holidays import FetchHolidays

router = APIRouter()

@router.get("/holidays", response_model=Holidays)
async def get_holidays(db: Session = Depends(get_db)):
  calendar_repository = SqlAlchemyCalendarRepository(db)
  fetch_holidays = FetchHolidays(calendar_repository)

  holidays = await fetch_holidays.execute()

  return {"holidays": holidays}

@router.post("/holidays", response_model=Holidays)
async def post_holidays(holidays: Holidays, db: Session = Depends(get_db)):
  calendar_repository = SqlAlchemyCalendarRepository(db)
  store_holidays = StoreHolidays(calendar_repository)
  calendars = []
  for holiday in holidays.holidays:
    calendar = Calendar(date=holiday, is_holiday=True)
    calendars.append(calendar)
  await store_holidays.execute(calendars)
  return holidays