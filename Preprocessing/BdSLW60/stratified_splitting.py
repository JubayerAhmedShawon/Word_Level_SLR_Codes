import os
import shutil
import pathlib
import random
from collections import defaultdict

# Define the root directory for your dataset
dataset_root_path = r"C:\Users\shawo\Desktop\Dextop new\BdSLW60 Full DataSet\FrameRate Corrected Clips"
output_root_path = r"C:\Users\shawo\Desktop\Dextop new\BdSLW60 Full DataSet"

# Create directory structure for train, test, and validation sets
os.makedirs(os.path.join(output_root_path, "train"), exist_ok=True)
os.makedirs(os.path.join(output_root_path, "test"), exist_ok=True)
os.makedirs(os.path.join(output_root_path, "val"), exist_ok=True)

# Gather all video paths
all_video_file_paths = list(pathlib.Path(dataset_root_path).glob("*/**/*.mp4"))

# Initialize counts
train_count = 0
test_count = 0
val_count = 0

# Organize files by user and class
user_class_files = defaultdict(list)

# Group videos by class and user
for path in all_video_file_paths:
    class_name = str(path.parent.name)
    filename = os.path.basename(path)

    if 'U4' in filename or 'U8' in filename:  # For test data
        destination = os.path.join(output_root_path, "test", class_name)
        os.makedirs(destination, exist_ok=True)
        shutil.copy(str(path), os.path.join(destination, filename))
        test_count += 1
    else:  # For training and validation (all other users)
        user_id = filename.split('_')[0]  # Assuming user ID is part of the filename like "U1W1F_trial_0.mp4"
        user_class_files[(user_id, class_name)].append(path)

# Split each user's videos into train and validation
for (user_id, class_name), files in user_class_files.items():
    random.shuffle(files)
    val_size = int(0.10 * len(files))  # Take 10% or 15% for validation
    val_files = files[:val_size]
    train_files = files[val_size:]

    # Copy validation files
    val_destination = os.path.join(output_root_path, "val", class_name)
    os.makedirs(val_destination, exist_ok=True)
    for path in val_files:
        shutil.copy(str(path), os.path.join(val_destination, os.path.basename(path)))
        val_count += 1

    # Copy remaining files to train
    train_destination = os.path.join(output_root_path, "train", class_name)
    os.makedirs(train_destination, exist_ok=True)
    for path in train_files:
        shutil.copy(str(path), os.path.join(train_destination, os.path.basename(path)))
        train_count += 1

# Print summary
print(f"Total training videos copied: {train_count}")
print(f"Total validation videos copied: {val_count}")
print(f"Total test videos copied: {test_count}")
print(f"Total files processed: {len(all_video_file_paths)}")
