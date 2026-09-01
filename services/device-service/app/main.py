from fastapi import FastAPI

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