from app.models.device import Device


class DeviceRepository:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    def get_all(self) -> list[Device]:
        return list(self.devices.values())

    def get_by_id(self, device_id: str) -> Device | None:
        return self.devices.get(device_id)

    def save(self, device: Device) -> Device:
        self.devices[device.id] = device
        return device