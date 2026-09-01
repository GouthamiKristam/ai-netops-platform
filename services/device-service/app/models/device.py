from pydantic import BaseModel, Field


class Device(BaseModel):
    id: str
    name: str
    ip_address: str
    device_type: str
    environment: str
    status: str = "healthy"


class DeviceCreate(BaseModel):
    name: str = Field(min_length=1)
    ip_address: str
    device_type: str
    environment: str