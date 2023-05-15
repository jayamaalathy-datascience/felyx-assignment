from fastapi import APIRouter
from config.db import conn
from models.reservation import reservations
from schemas.reservation import Reservation
from fastapi_pagination import Page, paginate


reservation = APIRouter()

@reservation.get('/')
def root_endpoint():
    return "API is running, Navigate to /docs for open API page"

@reservation.get(
    "/reservations",
    tags=["reservations"],
    response_model=Page[Reservation],
    description="Get a list of all reservations",
)
def get_reservations():
    all_reservations = conn.execute(reservations.select()).fetchall()
    return paginate(all_reservations)


@reservation.get(
    "/reservations/{id}",
    tags=["reservations"],
    response_model=Reservation,
    description="Get a reservations by Id",
)
def get_reservation(id: str):
    return conn.execute(reservations.select().where(reservations.c.ID == id)).first()


