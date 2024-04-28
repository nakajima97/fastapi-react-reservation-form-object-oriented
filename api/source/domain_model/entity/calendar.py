import datetime

from source.domain_model.value_object.id import Id

class Calendar():
    def __init__(
        self,
        id: Id,
        date: datetime.date,
        is_holiday: bool
    ):
        self.id = id
        self.date = date
        self.is_holiday = is_holiday

    def toDict(self):
        return {
            'id': self.id,
            'date': self.date,
            'is_holiday': self.is_holiday
        }