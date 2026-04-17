from fastapi import APIRouter 
import boto3

router = APIRouter()

@router.get("/")
def health_check():
    health_status = {"status": "healthy", "dependencies": {}}
    try:
        boto3.client('s3').list_buckets()
        health_status["dependencies"]["aws"] = "reachable"
    except Exception:
        health_status["dependencies"]["aws"] = "unreachable"
        health_status["status"] = "degraded"

    return health_status
