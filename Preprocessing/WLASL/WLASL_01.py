import os
import json
import shutil

# Load the JSON file
with open(r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\WLASL_v0.3.json", 'r') as f:
    data = json.load(f)

# Define the directory containing the MP4 files
mp4_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\videos"

# Define the output directory where you want to move the files
output_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\2000 Class"

# Loop through each gloss entry in the JSON data
for entry in data:
    gloss = entry['gloss']
    
    # Create a directory for each gloss
    gloss_directory = os.path.join(output_directory, gloss)
    os.makedirs(gloss_directory, exist_ok=True)
    
    # Loop through each instance of the gloss
    for instance in entry['instances']:
        video_id = instance['video_id']  # Assuming video_id corresponds to the MP4 filename without extension
        mp4_filename = f"{video_id}.mp4"
        src = os.path.join(mp4_directory, mp4_filename)
        
        if os.path.exists(src):
            # Move the MP4 file to the gloss directory
            dst = os.path.join(gloss_directory, mp4_filename)
            shutil.move(src, dst)
            print(f"Moved {mp4_filename} to {gloss_directory}")
        else:
            print(f"File {mp4_filename} not found in {mp4_directory}")
