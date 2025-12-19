# pip install opencv-python

import json
import cv2
import os
from concurrent.futures import ThreadPoolExecutor

def process_video(video_file_name, video_details, output_base_dir, video_path, orientation):
    print(f"Processing video: {video_path}")  # Debugging statement

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}.")
        return

    # Use the video file name (without extension) as the directory name
    video_name = os.path.splitext(video_file_name)[0]
    video_output_dir = os.path.join(output_base_dir, video_name)
    os.makedirs(video_output_dir, exist_ok=True)

    trials = video_details['trials']

    # Determine suffix based on orientation
    orientation_suffix = "_L" if orientation == "LeftHand" else "_R"

    # Iterate through trials and extract frames
    for trial_num, trial_details in trials.items():
        start_frame = trial_details['starting']
        end_frame = trial_details['ending']

        # Set the video to the starting frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        # Create a directory for each trial with orientation suffix in the name
        trial_output_dir = os.path.join(video_output_dir, f'trial_{trial_num}{orientation_suffix}')
        os.makedirs(trial_output_dir, exist_ok=True)

        # Extract and process frames within the trial range
        for frame_num in range(start_frame, end_frame + 1):
            ret, frame = cap.read()
            if not ret:
                print(f"Error: Could not read frame {frame_num} from {video_path}.")
                break

            # Save the frame as an image file with orientation suffix
            output_filename = os.path.join(trial_output_dir, f'frame_{frame_num}{orientation_suffix}.png')
            cv2.imwrite(output_filename, frame)
            print(f"Saved {output_filename}")

    # Release the video capture object for the current video
    cap.release()

def main():
    # Root directory containing subdirectories with JSON files and video files
    root_dir = r"D:\shawon\New folder" 

    # Base directory to save extracted frames
    output_base_dir = r"D:\shawon\FRAMES"
    os.makedirs(output_base_dir, exist_ok=True)

    # Use ThreadPoolExecutor to process multiple videos concurrently
    with ThreadPoolExecutor() as executor:
        futures = []

        # Iterate through subdirectories in the root directory
        for subdir in os.listdir(root_dir):
            subdir_path = os.path.join(root_dir, subdir)
            if os.path.isdir(subdir_path):
                # Find the JSON file in the current subdirectory
                json_file = None
                for file in os.listdir(subdir_path):
                    if file.endswith('.json'):
                        json_file = os.path.join(subdir_path, file)
                        break

                if json_file:
                    # Load JSON file
                    with open(json_file, 'r') as file:
                        data = json.load(file)

                    # Collect all video files from the current subdirectory
                    video_files = [f for f in os.listdir(subdir_path) if f.endswith('.mp4')]

                    # Create a mapping from video file names to their full paths
                    video_file_map = {os.path.splitext(os.path.basename(f))[0]: os.path.join(subdir_path, f) for f in video_files}

                    # Process each video as per the JSON details
                    for session, users in data.items(): # W1 - W60
                        for user, orientations in users.items(): # U1 - U18
                            for orientation, videos in orientations.items(): # L or R
                                for video_file_name, video_details in videos.items(): # trials [0:j]
                                    if video_file_name in video_file_map:
                                        video_path = video_file_map[video_file_name]
                                        futures.append(
                                            executor.submit(process_video, video_file_name + '.mp4', video_details, output_base_dir, video_path, orientation)
                                        )

        # Wait for all futures to complete
        for future in futures:
            future.result()

if __name__ == '__main__':
    main()
