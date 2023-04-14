from config.db import conn
from fastapi import APIRouter
from models.reservation import reservations
from shapely import wkb
from shapely.geometry import Point

import pandas as pd

location = APIRouter()

df = pd.read_csv("locations.csv")


@location.get("/locations/{id}",
              tags=["rides count"],
              description="Get Count of rides per location id", )
def root_endpoint(id: int):
    try:
        if id > 0:
            polygonal_hex = df.iloc[id - 1]['wgs84_polygon']
            polygon = wkb.loads(polygonal_hex, hex=True)
            all_reservations = conn.execute(reservations.select()).fetchall()
            count = 0
            for reservation in all_reservations:
                x = Point(reservation[4], reservation[5])
                if x.within(polygon):
                    count += 1
            return count
    except IndexError as e:
        return "location not found"
