import boto3
from datetime import datetime, timezone, timedelta

def get_bucket_info():
    s3_client = boto3.client('s3')

    buckets = s3_client.list_buckets()["Buckets"]
    current_date = datetime.now(timezone.utc).astimezone()

    old_buckets = []
    new_buckets = []

    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_date - timedelta(days=90)
        
        if creation_date < days_ago_90:
            old_buckets.append(bucket_name)
        else :
            new_buckets.append(bucket_name)

    return {
        "Total Buckets" : len(buckets),
        "New Buckets" : len(new_buckets),
        "Old Buckets" : len(old_buckets),
        "New Bucket Names": new_buckets,
        "Old Bucket Names": old_buckets,
    }

def audit_iam_keys():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    audit_report = []

    for user in users:
        keys = iam.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
        for key in keys:
            create_date = key['CreateDate']
            age_days = (datetime.now(timezone.utc) - create_date).days
            audit_report.append({
                "user_name": user['UserName'],
                "access_key_id": key['AccessKeyId'],
                "status": key['Status'],
                "age_days": age_days,
                "needs_rotation": age_days > 90
            })
    return audit_report

