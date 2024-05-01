from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from source.db import get_db
from source.schemas.reservations import Reservation as ReservationSchema, ResponseReservation, GetReservationResponse
from source.domain_model.usecase.reservation.store_reservation import StoreReservation
from source.domain_model.usecase.reservation.fetch_reservations import FetchReservations
from source.domain_model.repository.sqlalchemy_reservation_repository import SqlAlchemyReservationRepository
from source.domain_model.entity.reservation import Reservation

router = APIRouter()

@router.get("/reservations", response_model=GetReservationResponse)
async def get_reservations(db: Session = Depends(get_db)):
    sqlAlchemyReservationRepository = SqlAlchemyReservationRepository(db)
    fetch_reservations = FetchReservations(sqlAlchemyReservationRepository)
    result = await fetch_reservations.execute()
    return {"reservations": result}

@router.post("/reservations", response_model=ResponseReservation)
async def create_reservation(reservation_schema: ReservationSchema, db: Session = Depends(get_db)):
    sqlAlchemyReservationRepository = SqlAlchemyReservationRepository(db)
    storeReservation = StoreReservation(sqlAlchemyReservationRepository)

    reservation = Reservation(name = reservation_schema.name, reservation_date = reservation_schema.date, email_address = reservation_schema.email_address, phone_number = reservation_schema.phone_number)

    result = await storeReservation.execute(reservation)
    return result