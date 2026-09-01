from app.models.device import Device, DeviceCreate
from app.repositories.device_repository import DeviceRepository


class DeviceService:
    def __init__(self, repository: DeviceRepository):
        self.repository = repository

    def get_devices(self) -> list[Device]:
        return self.repository.get_all()

    def get_device(self, device_id: str) -> Device | None:
        return self.repository.get_by_id(device_id)

    def create_device(self, device_data: DeviceCreate) -> Device:
        device = Device(
            id=device_data.name,
            name=device_data.name,
            ip_address=device_data.ip_address,
            device_type=device_data.device_type,
            environment=device_data.environment,
        )

        return self.repository.save(device)