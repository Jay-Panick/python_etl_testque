import os
import shutil
from config import get_source_folder, get_destination_folder

def copy_folders():
    source = get_source_folder()
    destination = get_destination_folder()
    
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

if __name__ == "__main__":
    copy_folders()
