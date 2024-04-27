from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from source.models.reservations import Reservations as ReservationModel
from source.domain_model.entity.reservation import Reservation

class SqlAlchemyReservationRepository():
    def __init__(self, db: Session) -> None:
        self.db = db

    def __toModel(self, reservation: Reservation) -> ReservationModel:
        return ReservationModel(**reservation.toDict())

    async def insert(self, reservation: Reservation) -> ReservationModel:
        model = self.__toModel(reservation)
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return model

    async def fetch(self) -> List[ReservationModel]:
        result = await self.db.execute(select(ReservationModel))
        result_all = result.all()
        return [reservation[0] for reservation in result_all]