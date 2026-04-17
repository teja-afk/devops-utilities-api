from fastapi import FastAPI
from app.api import aws, metrics

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utilities APP for monitoring metrics, AWS Usuage, Log Analysis, etc",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")
