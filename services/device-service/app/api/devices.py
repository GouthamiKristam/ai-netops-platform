from fastapi import APIRouter, HTTPException

from app.models.device import Device, DeviceCreate
from app.repositories.device_repository import DeviceRepository
from app.services.device_service import DeviceService


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)

repository = DeviceRepository()
service = DeviceService(repository)


@router.get("/", response_model=list[Device])
def get_devices():
    return service.get_devices()


@router.get("/{device_id}", response_model=Device)
def get_device(device_id: str):
    device = service.get_device(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post("/", response_model=Device, status_code=201)
def create_device(device_data: DeviceCreate):
    return service.create_device(device_data)