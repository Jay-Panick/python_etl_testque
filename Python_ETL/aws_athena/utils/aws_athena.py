# utils/athena_query.py

import boto3
import time

def run_athena_query(query, database, s3_output, aws_access_key, aws_secret_key, region):
    client = boto3.client(
        'athena',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )

    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': database},
        ResultConfiguration={'OutputLocation': s3_output}
    )

    query_execution_id = response['QueryExecutionId']
    
    # Wait for the query to complete
    while True:
        result = client.get_query_execution(QueryExecutionId=query_execution_id)
        status = result['QueryExecution']['Status']['State']
        
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        time.sleep(5)

    if status == 'SUCCEEDED':
        s3_output_path = result['QueryExecution']['ResultConfiguration']['OutputLocation']
        return s3_output_path
    else:
        raise Exception(f"Query {query_execution_id} failed with status {status}")
