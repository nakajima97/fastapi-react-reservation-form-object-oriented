from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from source.db import get_db
from source.schemas.holidays import Holidays

router = APIRouter()

@router.get("/holidays", response_model=Holidays)
async def get_holidays(db: Session = Depends(get_db)):
  return {"holidays": ['2024-05-10', '2024-05-11']}

@router.post("/holidays", response_model=Holidays)
async def post_holidays(holidays: Holidays, db: Session = Depends(get_db)):
  return {"holidays": ['2024-05-10']}