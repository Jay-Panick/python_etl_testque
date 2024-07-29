# utils/manage_data.py

import os
from utils.helpers import clear_old_data

def manage_data(local_storage, days_to_keep):
    clear_old_data(local_storage, days_to_keep)
    # Additional logic for managing data if needed
