from fastapi import APIRouter

from source.schemas.calendars import CreateCalendarsRequest

router = APIRouter()

@router.post('/calendars')
async def create_calendar(create_calendar_request: CreateCalendarsRequest):
    return {'message': 'Create calendar'}