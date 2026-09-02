# Dependency Injection

## Overview

The Device Service uses FastAPI dependency injection to provide the service and repository layers to API endpoints.

The request flow is:

Client  
→ FastAPI API  
→ Dependency Injection  
→ DeviceService  
→ DeviceRepository

## Why Dependency Injection?

Dependency injection reduces coupling between the API layer and its implementation dependencies.

Instead of the API endpoint directly creating a `DeviceService` or `DeviceRepository`, FastAPI provides these dependencies.

This makes the design easier to:

- Test
- Extend
- Maintain
- Replace implementations
- Integrate with external infrastructure such as PostgreSQL

## Repository Lifecycle

The current implementation uses an in-memory repository.

The repository instance is provided through the dependency:

```python
repository = DeviceRepository()


def get_repository() -> DeviceRepository:
    return repository