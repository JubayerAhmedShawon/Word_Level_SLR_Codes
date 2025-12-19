import os
import cv2

# Define the source directory containing subdirectories with MP4 files
source_directory = r"C:\Users\shawo\Desktop\WLASL\wlasl_resized\wlasl-complete\2000 Class"

# Define the output directory to save the frames
output_directory = r"D:\shawon\WLASL\Frames"

# Iterate over each subdirectory and file
for subdir, _, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.mp4'):
            # Construct the full path to the MP4 file
            video_path = os.path.join(subdir, file)
            
            # Create the corresponding directory in the output folder
            relative_path = os.path.relpath(subdir, source_directory)  # Preserve original structure
            frame_output_dir = os.path.join(output_directory, relative_path, os.path.splitext(file)[0])
            os.makedirs(frame_output_dir, exist_ok=True)
            
            # Read the video file
            cap = cv2.VideoCapture(video_path)
            frame_count = 0
            success, frame = cap.read()
            
            while success:
                # Save frame as an image
                frame_filename = os.path.join(frame_output_dir, f"f{frame_count + 1}.png")
                cv2.imwrite(frame_filename, frame)
                
                # Read the next frame
                success, frame = cap.read()
                frame_count += 1
            
            cap.release()
            print(f"Extracted {frame_count} frames from {video_path} into {frame_output_dir}")
