from fastapi import FastAPI
from fastapi_pagination import add_pagination
from routes.reservation import reservation
from routes.location import location

app = FastAPI(
    title='Felyx API', description='APIs for Felyx Assignment', version='0.1')

app.include_router(reservation)
app.include_router(location)

add_pagination(app)
