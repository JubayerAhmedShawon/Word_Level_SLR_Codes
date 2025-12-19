# import os
# import shutil
# import json

# # Paths
# json_path = r"E:\WLASL\wlasl_resized\wlasl-complete\nslt_2000.json"
# root_dir = r"E:\WLASL\wlasl_resized\wlasl-complete\videos"
# output_dir = r"E:\WLASL\wlasl_resized\wlasl-complete\2000"

# # Load JSON
# with open(json_path, 'r') as f:
#     data = json.load(f)

# # Create output folders
# for subset in ['train', 'val', 'test']:
#     os.makedirs(os.path.join(output_dir, subset), exist_ok=True)

# # Process each video in the JSON file
# for video_id, details in data.items():
#     subset = details['subset']
#     video_filename = f"{video_id}.mp4"  # Assuming video files are named by ID
#     source_path = os.path.join(root_dir, video_filename)
#     destination_path = os.path.join(output_dir, subset, video_filename)
    
#     # Copy file if it exists
#     if os.path.exists(source_path):
#         shutil.copy(source_path, destination_path)
#         print(f"Copied {video_filename} to {subset} folder.")
#     else:
#         print(f"Video {video_filename} not found in root directory!")

# print("File organization complete.")


import os
import shutil
import json

# Paths
json_path = r"E:\WLASL\wlasl_resized\wlasl-complete\WLASL_v0.3.json" # Path to the second JSON file
root_dir = r"E:\WLASL\wlasl_resized\wlasl-complete\2000" # Directory containing MP4 files



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


# import os
# import cv2
# import matplotlib.pyplot as plt

# # Path to the root directory containing train, val, and test folders
# root_dir = r"D:\shawon\wlasl_100_class"  # Directory containing MP4 files


# # Path to save the plot
# output_plot_path = r"D:\shawon\frame_count_vs_video.png"


# # Collect frame counts and video information
# frame_data = []  # List to store tuples of (frame_count, gloss_name, video_name)

# # Iterate through train, val, and test folders
# for split in ["train", "val", "test"]:
#     split_dir = os.path.join(root_dir, split)
#     if not os.path.exists(split_dir):
#         print(f"Folder {split_dir} does not exist. Skipping.")
#         continue

#     # Iterate over gloss subfolders
#     for gloss_folder in os.listdir(split_dir):
#         gloss_path = os.path.join(split_dir, gloss_folder)
#         if not os.path.isdir(gloss_path):
#             continue

#         # Iterate over MP4 files in the gloss folder
#         for file in os.listdir(gloss_path):
#             if file.endswith(".mp4"):
#                 video_path = os.path.join(gloss_path, file)

#                 # Open the video file using OpenCV
#                 video = cv2.VideoCapture(video_path)
#                 if not video.isOpened():
#                     print(f"Could not open {video_path}. Skipping.")
#                     continue

#                 # Get total frame count
#                 frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

#                 # Append frame count and video info to the list
#                 frame_data.append((frame_count, gloss_folder, f"{split}/{gloss_folder}/{file}"))

#                 video.release()

# # Sort the data by frame count (min to max)
# frame_data_sorted = sorted(frame_data, key=lambda x: x[0])

# # Extract sorted frame counts and corresponding glosses
# frame_counts_sorted = [x[0] for x in frame_data_sorted]
# video_names_sorted = [x[2] for x in frame_data_sorted]
# gloss_names_sorted = [x[1] for x in frame_data_sorted]

# # Plot the sorted frame counts vs. video indices
# if frame_counts_sorted:
#     plt.figure(figsize=(12, 8))
#     plt.plot(frame_counts_sorted, marker='o', linestyle='-', color='b', label='Frame Count (Sorted)')
#     plt.title("Sorted Frame Count vs. Video Index (Min to Max) -- WLASL 100")
#     plt.xlabel("Video Index")
#     plt.ylabel("Frame Count")
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#     plt.legend()

#     # Save the plot
#     plt.savefig(output_plot_path, dpi=300, bbox_inches='tight')
#     print(f"Figure saved to {output_plot_path}.")

#     # Display the plot
#     plt.show()
# else:
#     print("No MP4 files found to analyze.")




