from pydantic import BaseModel
from datetime import datetime

class Reservation(BaseModel):
    ID: int
    CUSTOMER_ID: int
    START_RESERVATION_TIME: datetime
    END_RESERVATION_TIME: datetime
    START_LONGITUDE: float
    START_LATITUDE: float

    class Config:
        orm_mode = True

