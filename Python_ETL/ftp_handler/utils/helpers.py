# utils/helpers.py

import os
import shutil
from datetime import datetime, timedelta

def get_previous_date():
    return (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def clear_old_data(path, days_to_keep):
    cutoff_date = datetime.now() - timedelta(days=days_to_keep)
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            file_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if file_time < cutoff_date:
                os.remove(file_path)

def clear_duplicates(file_path):
    # Implement logic to remove duplicates
    pass
