from typing import List

from source.domain_model.repository.sqlalchemy_reservation_repository import SqlAlchemyReservationRepository
from source.domain_model.entity.reservation import Reservation

class FetchReservations:
    def __init__(self, reservation_repository: SqlAlchemyReservationRepository):
        self.reservation_repository = reservation_repository

    def execute(self):
        return  self.reservation_repository.fetch()