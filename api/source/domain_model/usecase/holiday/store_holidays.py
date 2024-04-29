from source.domain_model.repository.sqlalchemy_calendar_repository import SqlAlchemyCalendarRepository
from source.domain_model.entity.calendar import Calendar

class StoreHolidays():
    def __init__(self, holiday_repository):
        self.holiday_repository = holiday_repository

    async def execute(self, holidays: list[Calendar]):
        await self.holiday_repository.insert(holidays)