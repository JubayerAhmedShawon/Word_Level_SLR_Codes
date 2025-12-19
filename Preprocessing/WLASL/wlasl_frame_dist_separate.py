import os
import cv2
import matplotlib.pyplot as plt


# --------------------------------------------------
# Root directory
# --------------------------------------------------
root_dir = r"E:\WLASL\wlasl_100_class\wlasl_100_class"

# Output directory for plots
output_dir = r"C:\Users\shawo\Desktop\MSc New Exp Data"
os.makedirs(output_dir, exist_ok=True)


# --------------------------------------------------
# Function to process a split and generate plot
# --------------------------------------------------
def plot_frame_distribution(split_name):
    split_dir = os.path.join(root_dir, split_name)
    if not os.path.exists(split_dir):
        print(f"{split_name} folder not found. Skipping.")
        return

    frame_data = []

    # Iterate over gloss folders
    for gloss_folder in os.listdir(split_dir):
        gloss_path = os.path.join(split_dir, gloss_folder)
        if not os.path.isdir(gloss_path):
            continue

        for file in os.listdir(gloss_path):
            if file.endswith(".mp4"):
                video_path = os.path.join(gloss_path, file)

                video = cv2.VideoCapture(video_path)
                if not video.isOpened():
                    print(f"Could not open {video_path}")
                    continue

                frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
                frame_data.append(frame_count)

                video.release()

    if not frame_data:
        print(f"No videos found in {split_name}")
        return

    # Sort frame counts
    frame_data_sorted = sorted(frame_data)

    # --------------------------------------------------
    # Plot
    # --------------------------------------------------
    plt.figure(figsize=(12, 8))
    plt.plot(frame_data_sorted, marker='o', linestyle='-')
    plt.title(f"Sorted Frame Count vs Video Index ({split_name.upper()}) — WLASL 100")
    plt.xlabel("Video Index")
    plt.ylabel("Frame Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    output_path = os.path.join(
        output_dir, f"wlasl_100_frame_count_vs_video_{split_name}.png"
    )
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"{split_name} plot saved to: {output_path}")


# --------------------------------------------------
# Generate plots for each split
# --------------------------------------------------
for split in ["train", "val", "test"]:
    plot_frame_distribution(split)
