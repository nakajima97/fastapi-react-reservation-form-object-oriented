from pydantic import BaseModel, Field
import datetime


class Calendar(BaseModel):
    id: int = Field(..., title="ID")
    date: datetime.date = Field(..., title="Date of the holiday")
    is_holiday: bool = Field(..., title="Is holiday or not")


class CreateCalendarsRequest(BaseModel):
    start_date: datetime.date = Field(..., title="Start date of the holiday")
    end_date: datetime.date = Field(..., title="End date of the holiday")

    model_config = {
        "json_schema_extra": {
            "examples": [{"start_date": "2024-05-01", "end_date": "2024-05-31"}]
        }
    }


class GetCalendarResponse(BaseModel):
    calendars: list[Calendar] = Field(..., title="List of calendars")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "calendars": [
                        {"id": 1, "date": "2024-05-01", "is_holiday": True},
                        {"id": 2, "date": "2024-05-02", "is_holiday": False},
                    ]
                }
            ]
        }
    }
