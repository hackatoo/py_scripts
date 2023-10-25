import boto3

def create_record_route53(dns_name, ip, hosted_zone_id):
    change_exist_record = boto3.client('route53')
    response = change_exist_record.change_resource_record_sets(
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': dns_name,
                        'ResourceRecords': [
                            {
                                'Value': ip,
                            },
                        ],
                        'TTL': 300,
                        'Type': 'A',
                    },
                },
            ],
        },
        HostedZoneId = hosted_zone_id,
    )


def delete_existing_dns_record(dns_name, ip, hosted_zone_id):
    client = boto3.client('route53')
    response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'DELETE',
                'ResourceRecordSet': {
                    'Name': dns_name,
                    'ResourceRecords': [
                        {
                            'Value': ip,
                        },
                    ],
                    'TTL': 300,
                    'Type': 'A',
                },
            },
        ],
    },
    HostedZoneId = hosted_zone_id,
    )
