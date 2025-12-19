import os
import json
import shutil

# Load the JSON file
json_path = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\WLASL_v0.3.json"
with open(json_path, 'r') as f:
    data = json.load(f)

# Define the directory containing the MP4 files
mp4_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\videos"

# Define the output directory
output_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\WLASL Dataset"


# Loop through each gloss entry in the JSON data
for entry in data:
    gloss = entry['gloss']
    
    # Loop through each instance of the gloss
    for instance in entry['instances']:
        split = instance.get('split')  # Get the split field ('train', 'val', or 'test')
        video_id = instance['video_id']
        
        if not split:
            print(f"No split defined for video {video_id} under gloss {gloss}. Skipping.")
            continue
        
        # Create the split directory (train, val, test)
        split_directory = os.path.join(output_directory, split)
        os.makedirs(split_directory, exist_ok=True)
        
        # Create the gloss subdirectory within the split directory
        gloss_directory = os.path.join(split_directory, gloss)
        os.makedirs(gloss_directory, exist_ok=True)
        
        # Copy the video file
        mp4_filename = f"{video_id}.mp4"
        src = os.path.join(mp4_directory, mp4_filename)
        dst = os.path.join(gloss_directory, mp4_filename)
        
        if os.path.exists(src):
            shutil.copy(src, dst)  # Copy instead of move
            print(f"Copied {mp4_filename} to {split}/{gloss}")
        else:
            print(f"File {mp4_filename} not found in {mp4_directory}")
