from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from source.db import get_db
from source.schemas.holidays import Holidays
from source.domain_model.repository.sqlalchemy_calendar_repository import SqlAlchemyCalendarRepository
from source.domain_model.entity.calendar import Calendar
from source.domain_model.usecase.store_holidays import StoreHolidays

router = APIRouter()

@router.get("/holidays", response_model=Holidays)
async def get_holidays(db: Session = Depends(get_db)):
  return {"holidays": ['2024-05-10', '2024-05-11']}

@router.post("/holidays", response_model=Holidays)
async def post_holidays(holidays: Holidays, db: Session = Depends(get_db)):
  calendar_repository = SqlAlchemyCalendarRepository(db)
  store_holidays = StoreHolidays(calendar_repository)
  calendars = []
  for holiday in holidays.holidays:
    calendar = Calendar(date=holiday, is_holiday=True)
    calendars.append(calendar)
  await store_holidays.execute(calendars)
  print(calendars)
  return holidays