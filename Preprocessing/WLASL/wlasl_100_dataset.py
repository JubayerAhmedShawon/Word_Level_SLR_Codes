import os
import shutil
import json

# Paths
json_path = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\nslt_100.json"
root_dir = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\videos"
output_dir = r"D:\shawon\wlasl_100"

# Load JSON
with open(json_path, 'r') as f:
    data = json.load(f)

# Create output folders
for subset in ['train', 'val', 'test']:
    os.makedirs(os.path.join(output_dir, subset), exist_ok=True)

# Process each video in the JSON file
for video_id, details in data.items():
    subset = details['subset']
    video_filename = f"{video_id}.mp4"  # Assuming video files are named by ID
    source_path = os.path.join(root_dir, video_filename)
    destination_path = os.path.join(output_dir, subset, video_filename)
    
    # Copy file if it exists
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f"Copied {video_filename} to {subset} folder.")
    else:
        print(f"Video {video_filename} not found in root directory!")

print("File organization complete.")


import os
import shutil
import json

# Paths
json_path = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\WLASL_v0.3.json" # Path to the second JSON file
root_dir = r"D:\shawon\wlasl_100"  # Directory containing MP4 files



# Load JSON
with open(json_path, 'r') as f:
    data = json.load(f)

# Process each gloss and its instances
for gloss_data in data:
    gloss = gloss_data["gloss"]
    instances = gloss_data["instances"]

    gloss_folder_created = False  # Track if a gloss folder is created for any split

    for instance in instances:
        video_id = instance["video_id"]
        split = instance["split"]  # e.g., 'train', 'val', 'test'
        video_filename = f"{video_id}.mp4"
        source_path = os.path.join(root_dir, split, video_filename)

        # Check if the video file exists
        if os.path.exists(source_path):
            # Create gloss folder if not already created
            gloss_folder = os.path.join(root_dir, split, gloss)
            if not os.path.exists(gloss_folder):
                os.makedirs(gloss_folder, exist_ok=True)
                gloss_folder_created = True

            # Move the file
            destination_path = os.path.join(gloss_folder, video_filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {video_filename} to {gloss_folder}.")

    # Skip gloss folder creation if no files are found
    if not gloss_folder_created:
        print(f"No files found for gloss '{gloss}'. Skipping folder creation.")

print("File reorganization complete.")


