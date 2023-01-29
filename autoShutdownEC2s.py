import boto3
import datetime

def lambda_handler(event, context):
    # Connect to EC2
    ec2 = boto3.client("ec2")

    # Get all instances
    instances = ec2.describe_instances()["Reservations"]

    # Loop through all instances
    for reservation in instances:
        instance = reservation["Instances"][0]

        # Check if instance has been running for 2 hours
        launch_time = instance["LaunchTime"]
        running_time = datetime.datetime.now(launch_time.tzinfo) - launch_time
        if running_time.total_seconds() >= 7200:
            # Stop the instance
            ec2.stop_instances(InstanceIds=[instance["InstanceId"]])
