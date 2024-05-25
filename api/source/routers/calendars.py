from fastapi import APIRouter, Depends
from source.db import get_db

from source.schemas.calendars import CreateCalendarsRequest
from source.domain_model.repository.sqlalchemy_calendar_repository import (
    SqlAlchemyCalendarRepository,
)
from source.domain_model.usecase.calendars.store_calendars_by_date import (
    StoreCalendarsByDate,
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
