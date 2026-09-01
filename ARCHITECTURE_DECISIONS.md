# Architecture Decisions

This document records the key architectural and technology decisions made for the AI NetOps Platform, including the reasoning and trade-offs behind each decision.

The purpose is to make the architecture transparent, explainable, and easy for other engineers to understand and contribute to.

---

## ADR-001: Use a Microservices Architecture

### Status

Accepted

### Decision

The backend will be designed as a collection of independently deployable microservices rather than a single monolithic application.

### Context

The platform is designed as a large-scale Network Operations Platform that may manage a large number of network devices, metrics, incidents, alerts, and AI-driven investigations.

Different capabilities have different scaling, deployment, and processing requirements.

### Initial Services

* Device Service
* Metrics Service
* Incident Service
* Alert Service
* Search Service
* AI Service

### Rationale

Microservices allow individual capabilities to:

* Scale independently
* Be deployed independently
* Evolve independently
* Isolate failures
* Have clear domain boundaries

### Trade-offs

Microservices introduce additional complexity such as:

* Network communication
* Distributed debugging
* Service discovery
* Data consistency challenges
* Deployment and operational overhead

For this project, the benefits of independent scalability and deployment outweigh the additional complexity.

---

## ADR-002: Use Python and FastAPI

### Status

Accepted

### Decision

Python with FastAPI will be used for backend microservices.

### Rationale

FastAPI provides:

* Strong request and response validation
* Automatic OpenAPI documentation
* Async support
* Good performance
* Clean API development
* Easy integration with Machine Learning and AI libraries

Python also provides a strong ecosystem for the ML and AI components of the platform.

---

## ADR-003: Containerize Each Service

### Status

Accepted

### Decision

Each backend microservice and frontend application will be packaged as an independent Docker container.

### Rationale

Containerization provides:

* Consistent runtime environments
* Independent deployment
* Portability
* Easier local development
* Independent scaling

The containers will eventually be deployed using cloud-based container orchestration.

---

## ADR-004: Use Machine Learning for Anomaly Detection

### Status

Accepted

### Decision

Machine Learning will be used to identify abnormal infrastructure behavior from operational metrics.

### Rationale

Traditional threshold-based monitoring can identify known conditions such as CPU > 80%.

ML-based anomaly detection can additionally identify unusual combinations or patterns across metrics such as:

* CPU utilization
* Memory utilization
* Latency
* Throughput
* Connections
* Error rates

The initial implementation will evaluate suitable anomaly detection techniques such as Isolation Forest.

---

## ADR-005: Use RAG and LLMs for Intelligent Investigation

### Status

Accepted

### Decision

A Retrieval-Augmented Generation (RAG) architecture will be used for the AI investigation capability.

### Rationale

The AI service should not rely only on the LLM's general knowledge.

It will retrieve relevant context from:

* Knowledge-base articles
* Historical incidents
* Operational logs
* Current infrastructure metrics

The retrieved context will then be provided to the LLM to generate a contextual investigation summary and potential remediation recommendations.

---

## ADR-006: Support Cloud-Native Deployment

### Status

Accepted

### Decision

The application will be designed for container orchestration and cloud deployment.

The target AWS architecture will use:

* Amazon ECR for container images
* Amazon ECS/Fargate for container orchestration
* Application Load Balancer for traffic distribution
* Auto Scaling for demand-based scaling

Kubernetes will also be used during the project to demonstrate portable container orchestration concepts.

---

## ADR-007: Keep the Frontend Independently Deployable

### Status

Accepted

### Decision

The frontend will initially be developed as a React application and later evolved into a Micro Frontend architecture.

### Rationale

The platform contains multiple independent business capabilities such as:

* Network dashboard
* Device management
* Incident management
* AI Copilot

A Micro Frontend architecture can allow these capabilities to evolve and deploy independently while being presented through a common application shell.

The Micro Frontend implementation will be introduced after the initial React application is functional.

---

## ADR-008: Build Locally Before Cloud Deployment

### Status

Accepted

### Decision

The platform will first be developed and validated locally using Docker and Kubernetes before being deployed to AWS.

### Rationale

This allows the application architecture, service communication, testing, and containerization to be validated without requiring continuous cloud infrastructure.

Once the local implementation is stable, the same containerized services can be deployed to AWS.

---

## Decision Log

| ADR     | Decision                   | Status   |
| ------- | -------------------------- | -------- |
| ADR-001 | Microservices architecture | Accepted |
| ADR-002 | Python + FastAPI           | Accepted |
| ADR-003 | Docker containers          | Accepted |
| ADR-004 | ML anomaly detection       | Accepted |
| ADR-005 | RAG + LLM                  | Accepted |
| ADR-006 | AWS container deployment   | Accepted |
| ADR-007 | Micro Frontends            | Accepted |
| ADR-008 | Local-first development    | Accepted |
