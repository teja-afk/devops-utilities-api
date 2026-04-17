from fastapi import APIRouter, HTTPException
from app.services.metrics_service import get_system_metrics
from app.models.metrics_schema import SystemMetricsResponse
from loguru import logger

router = APIRouter()

@router.get("/metrics", response_model=SystemMetricsResponse)
def read_metrics():
    logger.info("Fetching system metrics")
    try:
        data = get_system_metrics()
        if data.cpu_percentage > 80:
            logger.warning(f"High CPU Detected: {data.cpu_percentage}%")
        return data
    except Exception as e:
        logger.error(f"Metrics collection failed: {e}")        
        raise HTTPException(status_code=500, detail=f"Metrics Error: {str(e)}")
