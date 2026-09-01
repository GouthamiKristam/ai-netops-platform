# AI NetOps Platform

An AI-powered, cloud-native Network Operations Platform designed to help engineers monitor network infrastructure, detect abnormal behavior, investigate incidents, and identify potential root causes.

## 🎯 Project Goal

Large-scale network environments can contain hundreds or thousands of devices and services generating continuous operational data such as metrics, logs, alerts, and incidents.

When a problem occurs, engineers often need to manually correlate information from multiple sources to understand:

> **What happened, why did it happen, and what should I investigate or do next?**

The AI NetOps Platform aims to reduce this manual effort by combining real-time monitoring, Machine Learning-based anomaly detection, event-driven microservices, and an AI/RAG-powered investigation assistant.

The platform is designed as a realistic enterprise-scale application rather than a simple CRUD application.

---

## 💡 What Problem Are We Solving?

The platform addresses three key operational challenges:

### 1. Detecting abnormal behavior

Traditional monitoring systems often rely heavily on static thresholds.

For example:

```text
CPU > 80% → Alert
```

The platform will use Machine Learning to identify unusual patterns across multiple infrastructure metrics such as:

* CPU utilization
* Memory utilization
* Latency
* Throughput
* Connections
* Error rates

### 2. Reducing manual incident investigation

Operational information is distributed across:

* Metrics
* Logs
* Alerts
* Historical incidents
* Device information
* Knowledge-base documentation

The platform will correlate this information to provide engineers with a consolidated view of an incident.

### 3. Providing intelligent investigation assistance

An AI-powered investigation service will use Retrieval-Augmented Generation (RAG) to retrieve relevant operational context and provide:

* Incident summaries
* Supporting evidence
* Potential root causes
* Similar historical incidents
* Recommended investigation steps

---

# 🏗️ High-Level Architecture

```text
                              USERS
                                │
                                ▼
                       ┌─────────────────┐
                       │   React Shell   │
                       │  / Micro FE     │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  API Gateway    │
                       └────────┬────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │          │          │          │           │
          ▼          ▼          ▼          ▼           ▼
      Device      Metrics    Incident    Alert      AI/RAG
      Service     Service    Service     Service    Service
          │          │          │          │           │
          ▼          ▼          ▼          ▼           ▼
        Device    Metrics    Incident    Event      Vector
          DB        Store       DB       Store        DB
                                                        │
                                                        ▼
                                                       LLM

                     ┌──────────────────────┐
                     │   ML Anomaly         │
                     │   Detection Service   │
                     └──────────┬───────────┘
                                │
                                ▼
                         Anomaly Events
```

---

# 🧩 Core Services

| Service          | Responsibility                                |
| ---------------- | --------------------------------------------- |
| Device Service   | Manage network/load-balancer devices          |
| Metrics Service  | Collect and process infrastructure metrics    |
| Incident Service | Manage incidents and their lifecycle          |
| Alert Service    | Evaluate alert conditions and generate events |
| Search Service   | Search operational and historical information |
| ML Service       | Detect anomalous infrastructure behavior      |
| AI Service       | RAG-based investigation and recommendations   |

---

# 🤖 AI & Machine Learning

The platform intentionally uses **ML and Generative AI for different responsibilities**.

### Machine Learning — Detect

ML analyzes infrastructure metrics and identifies abnormal behavior.

```text
Metrics
   │
   ▼
Feature Engineering
   │
   ▼
Anomaly Detection Model
   │
   ▼
Anomaly Score
   │
   ▼
Incident / Alert
```

Potential initial approach:

**Isolation Forest**

---

### Generative AI + RAG — Investigate

Once an incident occurs:

```text
Incident
   │
   ├── Current Metrics
   ├── Logs
   ├── Historical Incidents
   └── Knowledge Base
             │
             ▼
        Retrieval
             │
             ▼
            RAG
             │
             ▼
            LLM
             │
             ▼
 Investigation Summary
 + Potential Root Cause
 + Recommended Actions
```

The AI is therefore not simply a chatbot. It is designed to provide **context-aware operational assistance**.

---

# 🖥️ Frontend

The frontend will initially be built using:

* React
* TypeScript
* Modern component architecture
* API-driven UI
* Data visualization

The application will initially be developed as a React application and later evolved into a **Micro Frontend architecture**.

Potential frontend domains:

```text
React Shell
   │
   ├── Dashboard Micro FE
   ├── Devices Micro FE
   ├── Incidents Micro FE
   └── AI Copilot Micro FE
```

---

# 🐍 Backend

Backend microservices will use:

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* Pytest

Each service will be independently deployable.

---

# 🐳 Containerization

Every application component will be packaged as a Docker container.

```text
FastAPI Service
      │
      ▼
Docker Image
      │
      ▼
Container
```

Docker Compose will initially be used for local development.

---

# ☸️ Orchestration

The application will be designed to run on container orchestration platforms.

Local/container orchestration:

**Kubernetes**

Cloud deployment:

**AWS ECS/Fargate**

The architecture will demonstrate concepts such as:

* Container scheduling
* Service discovery
* Health checks
* Horizontal scaling
* Load balancing
* Resource management

---

# ☁️ AWS Architecture

The target AWS deployment will use:

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Docker Build
   │
   ▼
Amazon ECR
   │
   ▼
Amazon ECS / Fargate
   │
   ▼
Application Load Balancer
   │
   ▼
Auto Scaling
```

The project will initially be developed and tested locally before cloud deployment.

---

# 🔄 CI/CD

GitHub Actions will eventually automate:

```text
Code Push
   │
   ▼
Unit Tests
   │
   ▼
Integration Tests
   │
   ▼
Docker Build
   │
   ▼
Security Scan
   │
   ▼
Container Registry
   │
   ▼
Deployment
```

---

# 📊 Observability

The platform will eventually include:

* Centralized logging
* Application metrics
* Health checks
* Distributed tracing
* Service monitoring

Potential technologies include:

* Prometheus
* Grafana
* OpenTelemetry

---

# 🔐 Security

Security considerations will include:

* Authentication
* Authorization / RBAC
* JWT-based access
* API validation
* Secrets management
* Container security
* Dependency scanning

---

# 🛠️ Technology Stack

| Area                  | Technology                           |
| --------------------- | ------------------------------------ |
| Frontend              | React + TypeScript                   |
| Backend               | Python + FastAPI                     |
| Database              | PostgreSQL                           |
| Containerization      | Docker                               |
| Local Orchestration   | Kubernetes                           |
| Cloud Orchestration   | AWS ECS/Fargate                      |
| Container Registry    | AWS ECR                              |
| Load Balancing        | AWS ALB                              |
| CI/CD                 | GitHub Actions                       |
| ML                    | Python / Scikit-learn                |
| GenAI                 | LLM + RAG                            |
| Vector Storage        | TBD                                  |
| Observability         | Prometheus / Grafana / OpenTelemetry |
| Frontend Architecture | Micro Frontends                      |

---

# 📚 Project Documentation

* [Architecture Decisions](ARCHITECTURE_DECISIONS.md)

Additional architecture, API, AI/ML, deployment, security, and observability documentation will be added as the project evolves.

---

# 🚧 Project Status

This project is being developed incrementally.

### Phase 1 — Foundation

* [x] Repository setup
* [x] Architecture definition
* [x] Architecture decisions
* [ ] Initial FastAPI service

### Phase 2 — Backend Microservices

* [ ] Device Service
* [ ] Metrics Service
* [ ] Incident Service
* [ ] Alert Service
* [ ] Search Service
* [ ] AI Service

### Phase 3 — ML

* [ ] Metric simulation
* [ ] Feature engineering
* [ ] Anomaly detection
* [ ] ML service integration

### Phase 4 — AI/RAG

* [ ] Knowledge base
* [ ] Embeddings
* [ ] Vector database
* [ ] RAG pipeline
* [ ] AI investigation service

### Phase 5 — Frontend

* [ ] React dashboard
* [ ] Device management
* [ ] Incident management
* [ ] AI Copilot

### Phase 6 — Micro Frontends

* [ ] React shell
* [ ] Dashboard Micro FE
* [ ] Incident Micro FE
* [ ] AI Copilot Micro FE

### Phase 7 — Deployment

* [ ] Docker Compose
* [ ] Kubernetes
* [ ] AWS ECR
* [ ] AWS ECS/Fargate
* [ ] ALB
* [ ] Auto Scaling

### Phase 8 — DevOps & Observability

* [ ] GitHub Actions CI/CD
* [ ] Monitoring
* [ ] Logging
* [ ] Distributed tracing
* [ ] Security scanning

---

# 🎯 Learning & Engineering Objectives

This project is intended to demonstrate practical experience across:

**Frontend Engineering → Micro Frontends → Backend Microservices → Distributed Systems → ML → Generative AI → Containers → Kubernetes → AWS → CI/CD → Observability**

The focus is not only on implementing individual technologies, but on understanding how they work together as part of a scalable enterprise application.
