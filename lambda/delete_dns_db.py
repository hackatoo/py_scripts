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
    
    dns_name = event.get('dns_name')
    
    try: 
        conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=token) #Открываем подключение к базе Postgres в RDS
        cur = conn.cursor() 
        cur.execute("DELETE FROM id_dns_ip.mapping WHERE dns_name = %s", (dns_name,))
        conn.commit()
    except Exception as e:
        print("Database connection failed due to {}".format(e))
    finally:
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")