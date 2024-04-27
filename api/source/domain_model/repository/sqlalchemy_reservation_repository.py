from sqlalchemy.orm import Session

from source.models.reservations import Reservations as ReservationModel
from source.domain_model.entity.reservation import Reservation

class SqlAlchemyReservationRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def __toModel(self, reservation: Reservation) -> ReservationModel:
        return ReservationModel(**reservation.toDict())

    async def insert(self, reservation: Reservation) -> ReservationModel:
        model = self.__toModel(reservation)
        if (model.id == 0):
            model.id = None
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return model