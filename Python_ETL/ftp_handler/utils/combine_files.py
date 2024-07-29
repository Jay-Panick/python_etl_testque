import os
import pandas as pd
from config import get_destination_folder

def combine_files():
    base_path = get_destination_folder()
    fcs_files = []
    hgb_files = []
    
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith('.fcs'):
                fcs_files.append(os.path.join(root, file))
            elif file.endswith('.hgb'):
                hgb_files.append(os.path.join(root, file))
    
    combined_data = []
    
    for fcs_file in fcs_files:
        data = pd.read_csv(fcs_file)
        combined_data.append(data)
    
    for hgb_file in hgb_files:
        data = pd.read_csv(hgb_file)
        combined_data.append(data)
    
    if combined_data:
        combined_df = pd.concat(combined_data, ignore_index=True)
        combined_df.to_csv(os.path.join(base_path, 'combined_data.csv'), index=False)

if __name__ == "__main__":
    combine_files()
