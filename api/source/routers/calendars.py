from fastapi import APIRouter, Depends
from source.db import get_db
from datetime import datetime

from source.schemas.calendars import CreateCalendarsRequest, GetCalendarResponse
from source.domain_model.repository.sqlalchemy_calendar_repository import (
    SqlAlchemyCalendarRepository,
)
from source.domain_model.usecase.calendars.store_calendars_by_date import (
    StoreCalendarsByDate,
)
from source.domain_model.usecase.calendars.fetch_calendars_by_date import (
    FetchCalendarsByDate,
)
router = APIRouter()


@router.post("/calendars")
async def create_calendar(
    create_calendar_request: CreateCalendarsRequest, db=Depends(get_db)
):
    calendar_repository = SqlAlchemyCalendarRepository(db)
    store_calendars_by_date = StoreCalendarsByDate(calendar_repository)

    await store_calendars_by_date.execute(
        create_calendar_request.start_date, create_calendar_request.end_date
    )

    return {"message": "Create calendar"}

@router.get("/calendars")
async def fetch_calendar(
    start_date: str, end_date: str, db=Depends(get_db)
):
    calendar_repository = SqlAlchemyCalendarRepository(db)
    fetch_calendars_by_date = FetchCalendarsByDate(calendar_repository)

    parameter_date_format = "%Y-%m-%d"
    calendars = await fetch_calendars_by_date.execute(datetime.strptime(start_date, parameter_date_format), datetime.strptime(end_date, parameter_date_format))

    return calendars