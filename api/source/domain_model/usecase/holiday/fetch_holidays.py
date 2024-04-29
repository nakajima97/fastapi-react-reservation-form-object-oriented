from source.domain_model.repository.sqlalchemy_calendar_repository import SqlAlchemyCalendarRepository

class FetchHolidays():
    def __init__(self, calendar_repository: SqlAlchemyCalendarRepository) -> None:
        self.calendar_repository = calendar_repository

    async def execute(self) -> list:
        return await self.calendar_repository.fetch_holidays()