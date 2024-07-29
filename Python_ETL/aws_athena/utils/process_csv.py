# utils/process_csv.py

import pandas as pd
import os

def add_columns_to_csv(file_path):
    df = pd.read_csv(file_path)
    # Example calculation columns
    df['new_column1'] = df['existing_column1'] * 2
    df['new_column2'] = df['existing_column2'] + 100
    df.to_csv(file_path, index=False)
