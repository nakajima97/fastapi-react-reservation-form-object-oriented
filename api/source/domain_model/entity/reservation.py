from source.domain_model.value_object.id import Id
from source.domain_model.value_object.name import Name
from source.domain_model.value_object.reservation_date import ReservationDate
from source.domain_model.value_object.email_address import EmailAddress
from source.domain_model.value_object.phone_number import PhoneNumber

class Reservation():
    def __init__(
        self,
        name: Name,
        reservation_date: ReservationDate,
        email_address: EmailAddress,
        phone_number: PhoneNumber,
        id: Id | None = None
    ) -> None:
        self.id = id
        self.name = name
        self.reservation_date = reservation_date
        self.email_address = email_address
        self.phone_number = phone_number

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.reservation_date,
            'email_address': self.email_address,
            'phone_number': self.phone_number
        }