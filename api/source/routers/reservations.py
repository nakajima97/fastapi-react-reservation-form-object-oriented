from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from source.db import get_db
from source.schemas.reservations import Reservation as ReservationSchema, ResponseReservation, GetReservationResponse
from source.domain_model.usecase.store_reservation import StoreReservation
from source.domain_model.repository.sqlalchemy_reservation_repository import SqlAlchemyReservationRepository
from source.domain_model.entity.reservation import Reservation

router = APIRouter()

@router.get("/reservations", response_model=GetReservationResponse)
async def get_reservations():
  return {
      "reservations": [
          {
              "id": 1,
              "date": "2024-04-13",
              "name": "John Doe",
              "email_address": "example@example.com",
              "phone_number": "123-4567-8901",
          },
          {
              "id": 2,
              "date": "2024-04-30",
              "name": "Deborah Doe",
              "email_address": "example@example.com",
              "phone_number": "123-4567-8901",
          },
      ]
  }

@router.post("/reservations", response_model=ResponseReservation)
async def create_reservation(reservation_schema: ReservationSchema, db: Session = Depends(get_db)):
    sqlAlchemyReservationRepository = SqlAlchemyReservationRepository(db)
    storeReservation = StoreReservation(sqlAlchemyReservationRepository)

    reservation = Reservation(id = 0, name = reservation_schema.name, reservation_date = reservation_schema.date, email_address = reservation_schema.email_address, phone_number = reservation_schema.phone_number)

    result = await storeReservation.execute(reservation)
    return result