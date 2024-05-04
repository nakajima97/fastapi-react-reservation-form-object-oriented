from source.domain_model.repository.sqlalchemy_reservation_repository import (
    SqlAlchemyReservationRepository,
)


class FetchReservations:
    def __init__(self, reservation_repository: SqlAlchemyReservationRepository):
        self.reservation_repository = reservation_repository

    def execute(self):
        return self.reservation_repository.fetch()
