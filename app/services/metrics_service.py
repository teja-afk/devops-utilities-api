import psutil
from app.models.metrics_schema import SystemMetricsResponse
from app.core.config import settings

def get_system_metrics() -> SystemMetricsResponse:
    # interval=0.1 provides a quick sample without blocking the API for a full second
    cpu_percent = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    threshold = settings.CPU_THRESHOLD # Ideally moved to a config file later
    
    return SystemMetricsResponse(
        cpu_percentage=cpu_percent,
        memory_percentage=memory,
        disk_percentage=disk,
        cpu_threshold=threshold,
        system_status="CPU HIGH" if cpu_percent > threshold else "Healthy"
    )
