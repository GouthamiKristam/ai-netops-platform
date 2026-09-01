from fastapi import FastAPI

from app.api.devices import router as devices_router


app = FastAPI(
    title="AI NetOps - Device Service",
    description="Microservice responsible for managing network devices.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "device-service",
    }


app.include_router(devices_router)