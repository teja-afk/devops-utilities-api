from pydantic import BaseModel
from typing import List

class S3BucketResponse(BaseModel):
    total_buckets: int
    new_buckets: int
    old_buckets: int
    new_bucket_names: List[str]
    old_bucket_names: List[str]

class IAMKeyAuditResponse(BaseModel):
    user_name: str
    access_key_id: str
    status: str
    age_days: int
    needs_rotation: bool
