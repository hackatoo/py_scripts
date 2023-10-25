import boto3
import json

REGION = ""
AMI_ID = ''
INSTANCE_NAME=''
SUBNET_ID = ''
SECURITY_GROUP_ID = ''
KEY = ''

ec2 = boto3.resource('ec2', region_name=REGION)

def lambda_handler(event, context):
    ec2.create_instances(
        ImageId=AMI_ID,
        InstanceType='t2.large',
        KeyName=KEY,
        SecurityGroupIds=[
            SECURITY_GROUP_ID,
        ],
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
        IamInstanceProfile={
            'Name': 'AmazonSSMRoleForInstancesQuickSetup'
        },
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': INSTANCE_NAME
                    },
                ]
            },
        ],
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'SnapshotId': 'snap-0601ee96e410b1664',
                    'VolumeSize': 50,
                    'VolumeType': 'gp2'
                },
                'NoDevice': ''
            },
        ],
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Server is launched!')