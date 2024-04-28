import datetime

class Calendar():
    def __init__(
        self,
        date: datetime.date,
        is_holiday: bool
    ):
        self.date = date
        self.is_holiday = is_holiday