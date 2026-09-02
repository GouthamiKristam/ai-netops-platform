## Local PostgreSQL Development

PostgreSQL will run locally using Docker during development and testing.

This approach allows the project to use a production-grade relational database without requiring:

- AWS infrastructure
- A paid cloud database
- An external PostgreSQL server

The local architecture is:

Developer Machine
    ↓
Docker
    ↓
PostgreSQL Container
    ↓
Device Service

This provides a consistent and reproducible local development environment.

The application architecture is designed so that the database can later be moved from the local Docker container to a managed cloud database such as Amazon RDS without requiring major changes to the business or API layers.

### Why Docker for Local PostgreSQL?

Docker provides:

- Reproducible database environments
- Easy setup and teardown
- Isolation from the host machine
- Consistent development across machines
- A deployment model similar to containerized production environments

### Cloud Migration

For production, PostgreSQL could be deployed using a managed database service such as Amazon RDS.

The intended evolution is:

Local Development:

FastAPI → Docker PostgreSQL

Production:

FastAPI Containers → Amazon RDS PostgreSQL

The application should not depend on whether PostgreSQL is running locally or in the cloud.