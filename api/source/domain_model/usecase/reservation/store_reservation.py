from source.domain_model.repository.sqlalchemy_reservation_repository import SqlAlchemyReservationRepository
from source.domain_model.entity.reservation import Reservation

class StoreReservation():
    def __init__(self, reservation_repository: SqlAlchemyReservationRepository):
        self.reservation_repository = reservation_repository

    async def execute(self, reservation: Reservation):
        return await self.reservation_repository.insert(reservation)