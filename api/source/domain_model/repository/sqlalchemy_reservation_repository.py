from sqlalchemy.orm import Session

from source.models.reservations import Reservation as SqlAlchemyReservation
from source.domain_model.entity.reservation import Reservation

class SqlAlchemyReservationRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def __toModel(self, reservation: Reservation) -> SqlAlchemyReservation:
        return SqlAlchemyReservation(reservation.toDict())

    async def create(self, reservation: Reservation) -> SqlAlchemyReservation:
        model = self.__toModel(reservation)
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return model