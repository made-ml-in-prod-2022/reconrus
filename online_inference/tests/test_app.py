from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


def test_predict():
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "age": 54,
                "sex": 1,
                "cp": 0,
                "trestbps": 140,
                "chol": 0,
                "fbs": 1,
                "restecg": 2,
                "thalach": 0,
                "exang": 1,
                "oldpeak": 1.3,
                "slope": 0,
                "ca": 2,
                "thal": 1,
            },
        )
    assert response.status_code == 200
    assert response.text == "0"


def test_incorrect_predict():
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "age": -5,
                "sex": 1,
                "cp": 6,
                "trestbps": 140,
                "chol": 0,
                "fbs": 1,
                "restecg": 160,
                "thalach": 0,
                "exang": -1.2,
                "oldpeak": 2,
                "slope": 0,
                "ca": 2,
                "thal": 1,
            },
        )
    assert response.status_code == 400
