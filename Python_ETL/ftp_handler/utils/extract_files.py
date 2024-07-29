import os
import zipfile
from config import get_destination_folder

def extract_files():
    base_path = get_destination_folder()
    
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(root)

if __name__ == "__main__":
    extract_files()
