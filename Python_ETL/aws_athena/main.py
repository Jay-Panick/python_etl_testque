# main.py

import os
from config import (
    NETWORK_LOCATION, LOCAL_STORAGE, LOG_STORAGE, DAYS_TO_KEEP, 
    AWS_REGION, S3_OUTPUT, ATHENA_DATABASE, ATHENA_QUERY, SHARED_DRIVE
)
from utils.copy_files import copy_files
from utils.extract_files import extract_files
from utils.combine_files import combine_files
from utils.manage_data import manage_data
from utils.aws_athena import run_athena_query, download_s3_file, get_s3_output_file
from utils.process_csv import add_columns_to_csv
from utils.helpers import get_previous_date, create_directory

def main():
    previous_date = get_previous_date()
    create_directory(LOCAL_STORAGE)
    create_directory(LOG_STORAGE)
    
    # Step 1: Copy folders from network location
    copy_files(NETWORK_LOCATION, LOCAL_STORAGE)
    
    # Step 2: Extract zip files
    extract_files(LOCAL_STORAGE, previous_date)
    
    # Step 3: Combine .fcs and .hgb files into CSV
    combine_files(LOCAL_STORAGE, previous_date)
    
    # Step 4: Run Athena query and download results
    query_execution_id = run_athena_query(ATHENA_QUERY, ATHENA_DATABASE, S3_OUTPUT, AWS_REGION)
    bucket, key = get_s3_output_file(S3_OUTPUT, query_execution_id)
    athena_file_path = os.path.join(LOCAL_STORAGE, previous_date, 'athena_data.csv')
    download_s3_file(bucket, key, athena_file_path)
    
    # Step 5: Add columns to CSV
    add_columns_to_csv(athena_file_path)
    
    # Step 6: Upload to shared drive
    shared_drive_path = os.path.join(SHARED_DRIVE, 'athena_data.csv')
    os.replace(athena_file_path, shared_drive_path)
    
    # Step 7: Manage old data
    manage_data(LOCAL_STORAGE, DAYS_TO_KEEP)

if __name__ == "__main__":
    main()
