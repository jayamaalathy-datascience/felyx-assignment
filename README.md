## Felyx Data Engineer Assignment

### Prerequisites
- docker

## Steps

### Run the database
- Run the `start-database.sh` script

This should pull the latest mysql script and start the mysql server in detached mode.

### Loading the data onto the database

- Run the `build-image` script to build the csv loader image
- Run the following cmd providing the csv file location to load the data onto the database
```shell
docker run -v {csv-path}:/data/input.csv -t felyx-reservation
```
where {csv-path} is the file location. In this case
```shell
docker run -v ./assignment_reservations.csv:/data/input.csv -t felyx-reservation
```

### Viewing the reservation data via API
- Run the `run-app` script with the felyx-reservation-api folder
- API is built with FastAPI and exposed at port 8000

### Running tests

- Run cmd `pytest` in `felyx-reservation-api` folder. 
