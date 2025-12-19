import os
import shutil

# Define the root directory containing the MP4 files
root_dir = r"C:\Users\shawo\Desktop\LSA64\60 fps\Cropped LSA64"

# Destination directories for train and test sets
train_dir = r"C:\Users\shawo\Desktop\LSA64\60 fps\train"
test_dir = r"C:\Users\shawo\Desktop\LSA64\60 fps\test"

# Create the train and test directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Iterate through the files in the root directory
for file_name in os.listdir(root_dir):
    if file_name.endswith(".mp4"):  # Process only MP4 files
        # Split the file name into parts
        parts = file_name.split("_")
        first_part = int(parts[0])  # Extract the first part (e.g., 001 → W1)
        second_part = parts[1]      # Extract the second part (e.g., 001 or 002)

        # Determine the destination folder (train or test)
        if second_part in ["001", "002"]:
            split_folder = test_dir
        else:
            split_folder = train_dir

        # Create the corresponding subfolder (e.g., W1 for 001, W2 for 002)
        subfolder_name = f"W{first_part}"
        subfolder_path = os.path.join(split_folder, subfolder_name)

        # Create the subfolder if it doesn't exist
        os.makedirs(subfolder_path, exist_ok=True)

        # Move the file to the appropriate subfolder
        shutil.move(os.path.join(root_dir, file_name), os.path.join(subfolder_path, file_name))

print("Files have been split into train and test sets successfully!")
