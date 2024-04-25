from source.domain_model.value_object.reservation_id import ReservationId
from source.domain_model.value_object.name import Name
from source.domain_model.value_object.reservation_date import ReservationDate
from source.domain_model.value_object.email_address import EmailAddress
from source.domain_model.value_object.phone_number import PhoneNumber

class Reservation():
    def __init__(
        self,
        id: ReservationId,
        name: Name,
        reservation_date: ReservationDate,
        email_address: EmailAddress,
        phone_number: PhoneNumber
    ) -> None:
        self.reservation_id = id
        self.name = name
        self.reservation_date = reservation_date
        self.email_address = email_address
        self.phone_number = phone_number