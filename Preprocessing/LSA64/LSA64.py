import os
import shutil

# Define the root directory containing the MP4 files
root_dir = r"C:\Users\shawo\Desktop\LSA64\Cropped LSA64"

# Destination root directory
dest_root = r"C:\Users\shawo\Desktop\LSA64\LSA64 Class"

# Create the destination directory if it doesn't exist
os.makedirs(dest_root, exist_ok=True)

# Iterate through the files in the root directory
for file_name in os.listdir(root_dir):
    if file_name.endswith(".mp4"):  # Process only MP4 files
        # Split the file name to get the first part before the first underscore
        first_part = file_name.split("_")[0]
        # Create the corresponding folder name (W1 for 001, W2 for 002, etc.)
        folder_name = f"W{int(first_part)}"
        # Create the full path for the destination folder
        dest_folder = os.path.join(dest_root, folder_name)
        # Create the destination folder if it doesn't exist
        os.makedirs(dest_folder, exist_ok=True)
        # Move the file to the destination folder
        shutil.move(os.path.join(root_dir, file_name), os.path.join(dest_folder, file_name))

print("Files have been organized into folders successfully!")
