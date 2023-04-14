from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_reservations_endpoint():
    response = client.get("/reservations")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1
    assert data["total"] == 1000
    assert data["size"] == 50


def test_particular_reservation():
    response = client.get("/reservations/21143965")
    assert response.status_code == 200
    assert response.json() == {"ID": 21143965,
                               "CUSTOMER_ID": 1128509,
                               "START_RESERVATION_TIME": "2023-01-02T00:20:52",
                               "END_RESERVATION_TIME": "2023-01-02T00:35:08",
                               "START_LATITUDE": 53.5703,
                               "START_LONGITUDE": 10.035
                               }
