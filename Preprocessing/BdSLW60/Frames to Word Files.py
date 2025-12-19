import os
import shutil
import re

# Path to the root directory
root_dir = r"D:\shawon\FRAMES"

# Base path for the destination directories
base_dest_dir = r"D:\shawon\words"

# Ensure base destination directory exists
os.makedirs(base_dest_dir, exist_ok=True)

# Walk through the root directory to find all folders
for dirpath, dirnames, _ in os.walk(root_dir):
    # Process each folder in the current directory level
    for folder in dirnames:
        # Use regex to find 'W' followed by digits in the folder name
        match = re.search(r'W(\d+)', folder)
        
        if match:
            # Extract the W number
            w_number = match.group(1)
            # Define the destination directory based on the W number
            dest_folder = os.path.join(base_dest_dir, f'W{w_number}')
            
            # Ensure the destination directory exists
            os.makedirs(dest_folder, exist_ok=True)
            
            # Move the folder to the destination directory
            shutil.move(os.path.join(dirpath, folder), os.path.join(dest_folder, folder))
            print(f"Moved folder {folder} to {dest_folder}")

print(f"All folders have been moved to their respective directories under {base_dest_dir}")
