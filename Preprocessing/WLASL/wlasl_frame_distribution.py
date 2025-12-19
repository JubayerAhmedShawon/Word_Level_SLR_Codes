import os
import cv2
import matplotlib.pyplot as plt

# Path to the root directory containing train, val, and test folders
root_dir = r"D:\shawon\wlasl_100_class"  # Directory containing MP4 files


# Path to save the plot
output_plot_path = r"D:\shawon\frame_count_vs_video.png"


# Collect frame counts and video information
frame_data = []  # List to store tuples of (frame_count, gloss_name, video_name)

# Iterate through train, val, and test folders
for split in ["train", "val", "test"]:
    split_dir = os.path.join(root_dir, split)
    if not os.path.exists(split_dir):
        print(f"Folder {split_dir} does not exist. Skipping.")
        continue

    # Iterate over gloss subfolders
    for gloss_folder in os.listdir(split_dir):
        gloss_path = os.path.join(split_dir, gloss_folder)
        if not os.path.isdir(gloss_path):
            continue

        # Iterate over MP4 files in the gloss folder
        for file in os.listdir(gloss_path):
            if file.endswith(".mp4"):
                video_path = os.path.join(gloss_path, file)

                # Open the video file using OpenCV
                video = cv2.VideoCapture(video_path)
                if not video.isOpened():
                    print(f"Could not open {video_path}. Skipping.")
                    continue

                # Get total frame count
                frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

                # Append frame count and video info to the list
                frame_data.append((frame_count, gloss_folder, f"{split}/{gloss_folder}/{file}"))

                video.release()

# Sort the data by frame count (min to max)
frame_data_sorted = sorted(frame_data, key=lambda x: x[0])

# Extract sorted frame counts and corresponding glosses
frame_counts_sorted = [x[0] for x in frame_data_sorted]
video_names_sorted = [x[2] for x in frame_data_sorted]
gloss_names_sorted = [x[1] for x in frame_data_sorted]

# Plot the sorted frame counts vs. video indices
if frame_counts_sorted:
    plt.figure(figsize=(12, 8))
    plt.plot(frame_counts_sorted, marker='o', linestyle='-', color='b', label='Frame Count (Sorted)')
    plt.title("Sorted Frame Count vs. Video Index (Min to Max) -- WLASL 100")
    plt.xlabel("Video Index")
    plt.ylabel("Frame Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    # Save the plot
    plt.savefig(output_plot_path, dpi=300, bbox_inches='tight')
    print(f"Figure saved to {output_plot_path}.")

    # Display the plot
    plt.show()
else:
    print("No MP4 files found to analyze.")




