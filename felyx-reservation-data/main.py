# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:20:33 2023

@author: Jayamaalathy Selvakumar
"""
import mysql.connector
from mysql.connector import Error

import pandas as pd

# Read the input supplied while running the docker image
df = pd.read_csv('/data/input.csv')
print("Read the data")

df.sort_values(by=['START_RESERVATION_TIME', 'END_RESERVATION_TIME'], inplace=True)
print("Sorting values based on reservation time")

try:
    # establishing the connection
    conn = mysql.connector.connect(user='root', password='felyx', host='host.docker.internal', database='felyxDB')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS reservations ( ID int, CUSTOMER_ID int, START_RESERVATION_TIME datetime,'
        'END_RESERVATION_TIME datetime,START_LATITUDE float,START_LONGITUDE float)')

    for index, row in df.iterrows():
        # converting to datetime to be compatible with MySQL datetime format
        start_reservation_time = pd.to_datetime(row['START_RESERVATION_TIME'])
        end_reservation_time = pd.to_datetime(row['END_RESERVATION_TIME'])
        # forming the insert query
        sql = 'INSERT INTO felyxDB.reservations VALUES(' + str(row["ID"]) + "," + str(row["CUSTOMER_ID"]) + ",'" \
              + str(start_reservation_time) + "','" + str(end_reservation_time) + "'," + str(row["START_LATITUDE"]) \
              + "," + str(row["START_LONGITUDE"]) + ")"
        cursor.execute(sql)
        conn.commit()
    print("completed adding data")
    # Closing the connection
    conn.close()
except Error as e:
    print("Error while connecting to MySQL", e)
