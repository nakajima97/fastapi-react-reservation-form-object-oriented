from fastapi import APIRouter
from source.schemas.reservations import Reservation, ResponseReservation, GetReservationResponse

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
async def create_reservation(reservation: Reservation):
    return {
        "id": 1,
        "date": "2024-04-13",
        "name": "John Doe",
        "email_address": "example@example.com",
        "phone_number": "123-4567-8901",
    }