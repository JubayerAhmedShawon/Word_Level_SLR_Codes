import os
import json
import shutil

def load_frame_rates(json_path):
    # Load JSON data and extract FrameRate for each FileName
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    frame_rate_dict = {}
    # Traverse through the JSON structure to extract FrameRate for each FileName
    for w_key, w_value in data.items():
        for user, orientations in w_value.items():
            for orientation, files in orientations.items():
                for file_name, details in files.items():
                    frame_rate = int(details.get("FrameRate", 0))  # Convert FrameRate to integer
                    frame_rate_dict[file_name] = frame_rate
    return frame_rate_dict

def duplicate_frames_in_trials(trial_folder, frame_rate):
    # Sort frames by numerical order, extracting numbers from filenames
    frames = sorted(
        [f for f in os.listdir(trial_folder) if f.startswith("frame")],
        key=lambda x: int(x.split("_")[1].split(".")[0])
    )
    
    if frame_rate == 30:
        # No duplication needed for 30 FPS
        print(f"No duplication needed for {trial_folder}. FrameRate: {frame_rate}")
    elif frame_rate == 15:
        # Duplicate all frames for 15 FPS
        for frame_file in frames:
            src = os.path.join(trial_folder, frame_file)
            dest = os.path.join(trial_folder, frame_file.replace(".png", "_d.png"))
            shutil.copy(src, dest)
            print(f"Duplicated {frame_file} to {dest}")
    elif frame_rate == 24:
        # Duplicate every 4th frame and the last frame for 24 FPS
        for i, frame_file in enumerate(frames, start=1):
            if i % 4 == 0 or i == len(frames):  # Check if it's every 4th frame or the last frame
                src = os.path.join(trial_folder, frame_file)
                dest = os.path.join(trial_folder, frame_file.replace(".png", "_d.png"))
                shutil.copy(src, dest)
                print(f"Duplicated {frame_file} to {dest}")


def process_directory(root_dir):
    for subdir in os.listdir(root_dir):
        subdir_path = os.path.join(root_dir, subdir)
        
        if os.path.isdir(subdir_path):
            # Look specifically for the output1.json file in the current subdir (e.g., W1, W2)
            json_file = "output1.json"
            json_path = os.path.join(subdir_path, json_file)
            
            if not os.path.exists(json_path):
                print(f"No JSON file found in {subdir_path}")
                continue
            
            frame_rate_dict = load_frame_rates(json_path)
            
            # Process each user folder (e.g., U1W2F, U2W3F) within W* folders
            for user_folder in os.listdir(subdir_path):
                user_folder_path = os.path.join(subdir_path, user_folder)
                
                if os.path.isdir(user_folder_path) and user_folder in frame_rate_dict:
                    frame_rate = frame_rate_dict[user_folder]  # Get the FrameRate from the JSON file
                    
                    # Process each trial folder (e.g., trial_0, trial_1) within user folder
                    for trial_folder in os.listdir(user_folder_path):
                        trial_path = os.path.join(user_folder_path, trial_folder)
                        if os.path.isdir(trial_path):
                            duplicate_frames_in_trials(trial_path, frame_rate)

# Example usage
root_directory = r"D:\shawon\Min_9 and Max_164\BdSLW60 FINAL FRAMES FOLDER"
process_directory(root_directory)
