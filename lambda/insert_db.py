from cmath import e
import psycopg2
import sys
import boto3
import os


def lambda_handler(event, context): 
    
    ENDPOINT=""
    PORT="5432"
    USER="postgres"
    REGION="eu-west-2"
    DBNAME=""
    token=''
    
    id_instances = event.get('id_instances')
    name_instances = event.get('name_instances')
    dns_name = event.get('dns_name')
    ip = event.get('ip')
    hosted_zone_id = event.get('hosted_zone_id')
    region = event.get('region')
    status_instances = event = event.get('status_instances')
    
    try: 
        conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=token) #Открываем подключение к базе Postgres в RDS
        cur = conn.cursor() 
        postgres_insert_query = "INSERT INTO id_dns_ip.mapping (id_instances, name_instances, dns_name, ip, hosted_zone_id, region, status_instances) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        record_to_insert = (id_instances, name_instances, dns_name, ip, hosted_zone_id, region, status_instances)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit() 
    except Exception as e:
        print("Database connection failed due to {}".format(e))
    finally:
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")
    return record_to_insert