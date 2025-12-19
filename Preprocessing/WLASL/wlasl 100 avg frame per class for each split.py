# import os
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np


# # --------------------------------------------------
# # Paths
# # --------------------------------------------------
# root_dir = r"E:\WLASL\wlasl_100_class\wlasl_100_class"

# # Output directory for plots
# output_dir = r"C:\Users\shawo\Desktop\MSc New Exp Data"
# os.makedirs(output_dir, exist_ok=True)


# # --------------------------------------------------
# # Function: Avg frame count per class
# # --------------------------------------------------
# def plot_avg_frames_per_class(split_name):
#     split_dir = os.path.join(root_dir, split_name)
#     if not os.path.exists(split_dir):
#         print(f"{split_name} folder not found. Skipping.")
#         return

#     class_frame_counts = {}  # {class_name: [frame_counts]}

#     for gloss_folder in os.listdir(split_dir):
#         gloss_path = os.path.join(split_dir, gloss_folder)
#         if not os.path.isdir(gloss_path):
#             continue

#         for file in os.listdir(gloss_path):
#             if file.endswith(".mp4"):
#                 video_path = os.path.join(gloss_path, file)

#                 video = cv2.VideoCapture(video_path)
#                 if not video.isOpened():
#                     continue

#                 frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
#                 video.release()

#                 class_frame_counts.setdefault(gloss_folder, []).append(frames)

#     if not class_frame_counts:
#         print(f"No videos found in {split_name}")
#         return

#     # Compute averages
#     classes = sorted(class_frame_counts.keys())
#     avg_frames = [
#         np.mean(class_frame_counts[c]) for c in classes
#     ]

#     # --------------------------------------------------
#     # Plot
#     # --------------------------------------------------
#     plt.figure(figsize=(14, 6))
#     plt.bar(classes, avg_frames)
#     plt.xticks(rotation=90)
#     plt.xlabel("Class")
#     plt.ylabel("Average Frame Count")
#     plt.title(f"Average Frames per Class ({split_name.upper()}) — WLASL 100")
#     plt.grid(axis="y", linestyle="--", alpha=0.6)

#     output_path = os.path.join(
#         output_dir, f"wlasl_100_avg_frames_per_class_{split_name}.png"
#     )
#     plt.savefig(output_path, dpi=300, bbox_inches="tight")
#     plt.show()

#     print(f"{split_name} bar plot saved to: {output_path}")


# # --------------------------------------------------
# # Generate plots
# # --------------------------------------------------
# for split in ["train", "val", "test"]:
#     plot_avg_frames_per_class(split)
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


# --------------------------------------------------
# Paths
# --------------------------------------------------
root_dir = r"E:\WLASL\wlasl_100_class\wlasl_100_class"

# Output directory for plots
output_dir = r"C:\Users\shawo\Desktop\MSc New Exp Data"
os.makedirs(output_dir, exist_ok=True)


# --------------------------------------------------
# Function: Avg frame count per class
# --------------------------------------------------
def plot_avg_frames_per_class(split_name):
    split_dir = os.path.join(root_dir, split_name)
    if not os.path.exists(split_dir):
        print(f"{split_name} folder not found. Skipping.")
        return

    class_frame_counts = {}  # {class_name: [frame_counts]}

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
    # Compute averages + sample counts
    # --------------------------------------------------
    classes = sorted(class_frame_counts.keys())

    avg_frames = []
    x_labels = []

    for cls in classes:
        frames = class_frame_counts[cls]
        avg_frames.append(np.mean(frames))
        x_labels.append(f"{cls} ({len(frames)})")

    # --------------------------------------------------
    # Plot
    # --------------------------------------------------
    plt.figure(figsize=(16, 6))
    plt.bar(x_labels, avg_frames)
    plt.xticks(rotation=90, ha='right')
    plt.xlabel("Classes (Number of Samples)")
    plt.ylabel("Average Frame Count")
    plt.title(f"Average Frames per Class ({split_name.upper()}) — WLASL 100")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    output_path = os.path.join(
        output_dir, f"wlasl_100_avg_frames_per_class_{split_name}.png"
    )
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"{split_name} bar plot saved to: {output_path}")


# --------------------------------------------------
# Generate plots
# --------------------------------------------------
for split in ["train", "val", "test"]:
    plot_avg_frames_per_class(split)
