# config.py

import os

# Network location
NETWORK_LOCATION = r"\\network\path\to\source"

# Local storage
LOCAL_STORAGE = os.path.join(os.path.dirname(__file__), 'data')

# Log storage
LOG_STORAGE = os.path.join(os.path.dirname(__file__), 'logs')

# Days to keep
DAYS_TO_KEEP = 365

