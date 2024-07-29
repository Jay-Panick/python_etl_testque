# main.py

import os
from config import NETWORK_LOCATION, LOCAL_STORAGE, LOG_STORAGE, DAYS_TO_KEEP
from utils.copy_files import copy_files
from utils.extract_files import extract_files
from utils.combine_files import combine_files
from utils.manage_data import manage_data
from utils.helpers import get_previous_date, create_directory

def main():
    previous_date = get_previous_date()
    create_directory(LOCAL_STORAGE)
    create_directory(LOG_STORAGE)

    copy_files(NETWORK_LOCATION, LOCAL_STORAGE)
    extract_files(LOCAL_STORAGE, previous_date)
    combine_files(LOCAL_STORAGE, previous_date)
    manage_data(LOCAL_STORAGE, DAYS_TO_KEEP)

if __name__ == "__main__":
    main()
