# test_app.py

from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_secret():
    client = app.test_client()
    response = client.get("/check-secret")
    assert response.status_code == 200