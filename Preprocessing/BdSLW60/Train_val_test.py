import os
import shutil
import pathlib
import cv2  # Import OpenCV for video processing

# Define the root directory for your dataset
dataset_root_path = r"D:\shawon\Corrected Frames\FrameRate Corrected Clips Eng Class"
output_root_path = r"D:\shawon\Corrected Frames\Train-Test-Val(U1)"

# Create the output directory structure
os.makedirs(os.path.join(output_root_path, "train"), exist_ok=True)
os.makedirs(os.path.join(output_root_path, "val"), exist_ok=True)
os.makedirs(os.path.join(output_root_path, "test"), exist_ok=True)

# Gather all video paths
all_video_file_paths = list(pathlib.Path(dataset_root_path).glob("*/**/*.mp4"))

# Initialize counters for lengths and counts
train_count = 0
val_count = 0
test_count = 0

# Copy all files to their respective directories and track counts
def copy_files_to_folders(file_paths):
    global train_count, val_count, test_count
    for path in file_paths:
        class_name = str(path.parent.name)  # Get the immediate parent directory name
        filename = os.path.basename(path)

        # Direct videos based on user identifiers
        if filename.startswith('U1') and filename[2:3] == 'W':  # For validation (exact match for U1)
            destination = os.path.join(output_root_path, "val", class_name)
            val_count += 1  # Increment validation count
        elif 'U4' in filename or 'U8' in filename:  # For test
            destination = os.path.join(output_root_path, "test", class_name)
            test_count += 1  # Increment test count
        else:  # For training (including U10, U11, U12, U15, etc.)
            destination = os.path.join(output_root_path, "train", class_name)
            train_count += 1  # Increment training count
        
        # Create class directory if it doesn't exist
        os.makedirs(destination, exist_ok=True)

        # Copy the file to the appropriate class directory
        shutil.copy(str(path), os.path.join(destination, os.path.basename(path)))

        # Log the copying process
        print(f"Copied {os.path.basename(path)} to {destination}")

# Process all files and copy them
copy_files_to_folders(all_video_file_paths)

# Print total counts of MP4 files in each category
print(f"Total training videos copied: {train_count}")
print(f"Total validation videos copied: {val_count}")
print(f"Total test videos copied: {test_count}")
print(f"Total files copied: {len(all_video_file_paths)}")
