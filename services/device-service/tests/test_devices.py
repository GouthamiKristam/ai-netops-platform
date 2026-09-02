import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api.devices import get_repository
from app.repositories.device_repository import DeviceRepository


@pytest.fixture
def client():
    repository = DeviceRepository()

    app.dependency_overrides[get_repository] = lambda: repository

    yield TestClient(app)

    app.dependency_overrides.clear()


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "device-service",
    }


def test_create_device(client):
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


def test_get_devices(client):
    device = {
        "name": "ADC-TEST-002",
        "ip_address": "10.10.1.21",
        "device_type": "load-balancer",
        "environment": "test",
    }

    client.post("/devices/", json=device)

    response = client.get("/devices/")

    assert response.status_code == 200

    devices = response.json()

    assert len(devices) == 1
    assert devices[0]["id"] == "ADC-TEST-002"


def test_get_device(client):
    device = {
        "name": "ADC-TEST-003",
        "ip_address": "10.10.1.22",
        "device_type": "load-balancer",
        "environment": "test",
    }

    client.post("/devices/", json=device)

    response = client.get("/devices/ADC-TEST-003")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == "ADC-TEST-003"


def test_get_unknown_device(client):
    response = client.get("/devices/DOES-NOT-EXIST")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Device not found"
    }