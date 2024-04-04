from fastapi.testclient import TestClient
from main import app

client = TestClient(app=app)

def test_retrieve_all_events():
    response = client.get("/event")
    assert response.status_code == 200


def test_about():
    response = client.get("/about")
    assert response.json() == {"message": "about page"}


def test_get_one_event():
    data = {
        "username": "yilongma@tesla.com",
        "password": "666"
    }
    response = client.post("/user/signin", data=data)
    access_token = response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = client.get("/event/1", headers=headers)
    assert response.status_code == 200

    data = response.json()
    assert data.get("title") == "string"
