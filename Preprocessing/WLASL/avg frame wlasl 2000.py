

import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

root_dir = r"E:\WLASL\wlasl_resized\wlasl-complete\WLASL Dataset"

# Output directory for plots
output_dir = r"C:\Users\shawo\Desktop\MSc New Exp Data"
os.makedirs(output_dir, exist_ok=True)

def plot_avg_frames_per_class_wlasl2000(split_name, step=100):
    split_dir = os.path.join(root_dir, split_name)
    if not os.path.exists(split_dir):
        print(f"{split_name} folder not found. Skipping.")
        return

    class_frame_counts = {}

    # --------------------------------------------------
    # Collect frame counts
    # --------------------------------------------------
    for gloss_folder in os.listdir(split_dir):
        gloss_path = os.path.join(split_dir, gloss_folder)
        if not os.path.isdir(gloss_path):
            continue

        for file in os.listdir(gloss_path):
            if file.endswith(".mp4"):
                video_path = os.path.join(gloss_path, file)

                video = cv2.VideoCapture(video_path)
                if not video.isOpened():
                    continue

                frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
                video.release()

                class_frame_counts.setdefault(gloss_folder, []).append(frames)

    if not class_frame_counts:
        print(f"No videos found in {split_name}")
        return

    # --------------------------------------------------
    # Sort classes
    # --------------------------------------------------
    classes = sorted(class_frame_counts.keys())

    avg_frames = []
    sample_counts = []

    for cls in classes:
        frames = class_frame_counts[cls]
        avg_frames.append(np.mean(frames))
        sample_counts.append(len(frames))

    # --------------------------------------------------
    # Plot bars for ALL classes
    # --------------------------------------------------
    x = np.arange(len(classes))

    plt.figure(figsize=(18, 6))
    plt.bar(x, avg_frames)
    plt.ylabel("Average Frame Count")
    plt.xlabel("Classes")
    plt.title(f"Average Frames per Class ({split_name.upper()}) — WLASL 2000")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # --------------------------------------------------
    # Show tick labels only for every 100th class
    # --------------------------------------------------
    tick_positions = np.arange(step - 1, len(classes), step)
    tick_labels = [
        f"{classes[i]} ({sample_counts[i]})" for i in tick_positions
    ]

    plt.xticks(tick_positions, tick_labels, rotation=90, ha="right")

    output_path = os.path.join(
        output_dir,
        f"wlasl_2000_avg_frames_per_class_all_classes_sparse_ticks_{split_name}.png"
    )

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"{split_name} plot saved to: {output_path}")

    
for split in ["train", "val", "test"]:
    plot_avg_frames_per_class_wlasl2000(split, step=100)
