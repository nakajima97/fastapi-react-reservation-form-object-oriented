from pydantic import BaseModel, Field
import datetime


class CreateCalendarsRequest(BaseModel):
    start_date: datetime.date = Field(..., title="Start date of the holiday")
    end_date: datetime.date = Field(..., title="End date of the holiday")

    model_config = {
        "json_schema_extra": {
            "examples": [{"start_date": "2024-05-01", "end_date": "2024-05-31"}]
        }
    }


class GetCalendarResponse(BaseModel):
    date: datetime.date = Field(..., title="Date of the holiday")
    is_holiday: bool = Field(..., title="Is holiday or not")

    model_config = {
        "json_schema_extra": {
            "examples": [[{"date": "2024-05-01", "is_holiday": True}]]
        }
    }
