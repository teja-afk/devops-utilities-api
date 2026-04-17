from pydantic import BaseModel

class SystemMetricsResponse(BaseModel):
    cpu_percentage: float
    memory_percentage: float
    disk_percentage: float
    cpu_threshold: int
    system_status: str
