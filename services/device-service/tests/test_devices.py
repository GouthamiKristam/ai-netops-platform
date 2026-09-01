from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "device-service",
    }


def test_create_device():
    device = {
        "name": "ADC-TEST-001",
        "ip_address": "10.10.1.20",
        "device_type": "load-balancer",
        "environment": "test",
    }

    response = client.post("/devices/", json=device)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == "ADC-TEST-001"
    assert data["name"] == "ADC-TEST-001"
    assert data["ip_address"] == "10.10.1.20"
    assert data["device_type"] == "load-balancer"
    assert data["environment"] == "test"
    assert data["status"] == "healthy"


def test_get_devices():
    response = client.get("/devices/")

    assert response.status_code == 200

    devices = response.json()

    assert len(devices) >= 1


def test_get_device():
    response = client.get("/devices/ADC-TEST-001")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == "ADC-TEST-001"


def test_get_unknown_device():
    response = client.get("/devices/DOES-NOT-EXIST")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Device not found"
    }