import os
import shutil
import random

# Define the root directory containing the MP4 files
root_dir = r"C:\Users\shawo\Desktop\LSA64\60 fps\Cropped LSA64"

# Destination directories for train and test sets
train_dir = r"C:\Users\shawo\Desktop\LSA64\60 fps\train_"
test_dir = r"C:\Users\shawo\Desktop\LSA64\60 fps\test_"

# Set the train-test split ratio
train_ratio = 0.8

# Create the train and test directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Gather all file paths and their corresponding folder structure
file_paths = []
for file_name in os.listdir(root_dir):
    if file_name.endswith(".mp4"):  # Process only MP4 files
        file_paths.append(file_name)

# Shuffle the files randomly
random.shuffle(file_paths)

# Calculate the split index
split_index = int(len(file_paths) * train_ratio)

# Split the files into train and test sets
train_files = file_paths[:split_index]
test_files = file_paths[split_index:]

# Function to move files while retaining folder structure
def move_files(files, dest_dir):
    for file_name in files:
        # Extract the first part to determine the subfolder
        first_part = int(file_name.split("_")[0])
        subfolder_name = f"W{first_part}"
        subfolder_path = os.path.join(dest_dir, subfolder_name)
        
        # Create the subfolder if it doesn't exist
        os.makedirs(subfolder_path, exist_ok=True)
        
        # Move the file to the corresponding subfolder
        shutil.move(os.path.join(root_dir, file_name), os.path.join(subfolder_path, file_name))

# Move files to train and test directories
move_files(train_files, train_dir)
move_files(test_files, test_dir)

print("Dataset has been split into train and test sets successfully!")
