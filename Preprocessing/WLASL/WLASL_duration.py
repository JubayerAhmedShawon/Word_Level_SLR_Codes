import os
import cv2
import json

# Define the source directory containing subdirectories with MP4 files
source_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\2000 Class"

# Dictionary to store video durations
video_durations = {}

# Iterate over each subdirectory and file
for subdir, _, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.mp4'):
            # Construct the full path to the MP4 file
            video_path = os.path.join(subdir, file)
            
            # Open the video file
            cap = cv2.VideoCapture(video_path)
            
            # Get the frame count and frame rate
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Calculate the video duration in seconds
            duration = frame_count / fps  # Duration in seconds
            video_durations[file] = duration  # Store the duration
            
            cap.release()
            print(f"Video {file} has duration {duration:.2f} seconds")

# Save the durations to a JSON file
duration_output_file = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\video_durations.json"
with open(duration_output_file, 'w') as f:
    json.dump(video_durations, f, indent=4)

print(f"Video durations saved to {duration_output_file}")
