# config.py

import os

# Network location
NETWORK_LOCATION = r"\\network\path\to\source"

# Local storage
LOCAL_STORAGE = os.path.join(os.path.dirname(__file__), 'data')

# Log storage
LOG_STORAGE = os.path.join(os.path.dirname(__file__), 'logs')

# S3 configuration
AWS_ACCESS_KEY = 'your-access-key'
AWS_SECRET_KEY = 'your-secret-key'
AWS_REGION = 'your-region'
S3_BUCKET = 'your-s3-bucket'
S3_OUTPUT_PATH = 'path/in/s3'

# Athena configuration
ATHENA_DATABASE = 'your-database'
ATHENA_QUERY = 'SELECT * FROM your_table WHERE date = DATE_SUB(CURRENT_DATE, INTERVAL 1 DAY)'

# Shared drive configuration
SHARED_DRIVE_PATH = r"\\shared\drive\path"

# Days to keep
DAYS_TO_KEEP = 365
