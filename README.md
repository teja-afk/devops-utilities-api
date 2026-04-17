
# DevOps Utilities API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A production-ready infrastructure management API built with FastAPI. This project provides critical system metrics and cloud governance tools designed for internal DevOps workflows.

## 🚀 Key Features

- **System Health Monitoring**: Real-time retrieval of CPU, Memory, and Disk metrics using `psutil`.
- **AWS S3 Governance**: Automated audit of S3 buckets to identify "Stale" resources based on a configurable retention policy.
- **Industry Standard Architecture**: Implements Pydantic schemas for data validation and `pydantic-settings` for environment management.
- **Dockerized Environment**: Multi-stage Docker build for secure and lightweight containerized deployments.
- **Automated Documentation**: Interactive API documentation via Swagger UI and ReDoc.

## 🛠 Project Structure

```text
DEVOPS-UTILITIES-API/
├── app/
│   ├── api/            # Route handlers (Endpoints)
│   ├── core/           # Configuration management (Settings)
│   ├── models/         # Pydantic Schemas (Data Validation)
│   ├── services/       # Business logic (AWS & System logic)
│   └── main.py         # FastAPI App initialization
├── main.py             # Root entry point for Uvicorn
├── Dockerfile          # Multi-stage production Docker image
├── .env                # Environment-specific variables (Ignored by Git)
└── requirements.txt    # Python dependencies
```

⚙️ Quick Start
1. Prerequisites

    Python 3.12+

    AWS Credentials (configured via aws configure or .env)

2. Local Setup
## Clone the repository
```git clone https://github.com/teja-afk/devops-utilities-api.git```

```cd devops-utilities-api```

## Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Start the application
python main.py

3. Running with Docker
## Build the image
docker build -t devops-api .

## Run the container
docker run -p 8000:8000 --env-file .env devops-api

🔐 Configuration

The application uses a .env file for configuration. Create one in the root directory:

```py
APP_NAME="DevOps Utilities API"
DEBUG=True
PORT=8000
CPU_THRESHOLD=10
S3_RETENTION_DAYS=90
```

📖 API Endpoints
| Method | Endpoint        | Description                      |
|-GET----|-/api/v1/metrics-|-Returns CPU, RAM, and Disk usage-|
| GET    | /api/v1/s3      | Lists new and old S3 buckets     |
| GET    | /docs           | Interactive Swagger UI           |
| GET    | /redoc          | Static API Documentation         |

