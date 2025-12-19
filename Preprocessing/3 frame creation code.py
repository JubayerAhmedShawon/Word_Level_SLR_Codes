import cv2
import os

# Path to the input MP4 file
input_video_path = r"C:\Users\shawo\Desktop\U10W38F_trial_5_R.mp4"
output_folder = r"C:\Users\shawo\Desktop\thesis paper writting"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Check if the video is opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the video frame rate (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS: {fps}")

# Frame interval
frame_interval = 10

# Initialize frame counter
frame_count = 0
frame_id = 0

while True:
    # Read a frame
    ret, frame = cap.read()
    
    # If the frame was read successfully
    if not ret:
        break
    
    # Check if the frame is at the required interval
    if frame_count % frame_interval == 0:
        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f'frame_{frame_id}.png')
        cv2.imwrite(frame_filename, frame)
        frame_id += 1

    frame_count += 1

# Release the video capture object
cap.release()

print(f"Frames saved in: {output_folder}")
