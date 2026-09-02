from fastapi import APIRouter, Depends, HTTPException

from app.models.device import Device, DeviceCreate
from app.repositories.device_repository import DeviceRepository
from app.services.device_service import DeviceService


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


repository = DeviceRepository()


def get_repository() -> DeviceRepository:
    return repository


def get_device_service(
    repository: DeviceRepository = Depends(get_repository),
) -> DeviceService:
    return DeviceService(repository)


@router.get("/", response_model=list[Device])
def get_devices(
    service: DeviceService = Depends(get_device_service),
):
    return service.get_devices()


@router.get("/{device_id}", response_model=Device)
def get_device(
    device_id: str,
    service: DeviceService = Depends(get_device_service),
):
    device = service.get_device(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.post("/", response_model=Device, status_code=201)
def create_device(
    device_data: DeviceCreate,
    service: DeviceService = Depends(get_device_service),
):
    return service.create_device(device_data)