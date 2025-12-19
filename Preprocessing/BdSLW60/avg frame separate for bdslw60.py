# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# # --------------------------------------------------
# # Paths
# # --------------------------------------------------
# root_dir = r"E:\Extra\shawon\BdSLW60 Full DataSet Version 2\Train-Test-Val(U1)-BdSLW60"
# save_folder = r"C:\Users\shawo\Desktop\MSc New Exp Data"
# os.makedirs(save_folder, exist_ok=True)

# sub_dirs = ['train', 'val', 'test']


# # --------------------------------------------------
# # Process each split separately
# # --------------------------------------------------
# for sub_dir in sub_dirs:
#     sub_dir_path = os.path.join(root_dir, sub_dir)
#     if not os.path.exists(sub_dir_path):
#         print(f"Skipping missing directory: {sub_dir_path}")
#         continue

#     class_frame_lists = {}  # {class_name: [frame_counts]}

#     # Iterate class folders
#     for class_dir in os.listdir(sub_dir_path):
#         class_path = os.path.join(sub_dir_path, class_dir)
#         if not os.path.isdir(class_path):
#             continue

#         for file in os.listdir(class_path):
#             if file.endswith('.mp4'):
#                 video_path = os.path.join(class_path, file)

#                 video = cv2.VideoCapture(video_path)
#                 if not video.isOpened():
#                     continue

#                 frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
#                 video.release()

#                 class_frame_lists.setdefault(class_dir, []).append(frame_count)

#     if not class_frame_lists:
#         print(f"No videos found in {sub_dir}")
#         continue

#     # Compute averages
#     classes = sorted(class_frame_lists.keys())
#     avg_frames = [
#         np.mean(class_frame_lists[c]) for c in classes
#     ]

#     # --------------------------------------------------
#     # Plot
#     # --------------------------------------------------
#     plt.figure(figsize=(14, 6))
#     plt.bar(classes, avg_frames)
#     plt.xlabel('Classes', fontsize=12)
#     plt.ylabel('Average Frame Count', fontsize=12)
#     plt.title(
#         f'Average Frames per Class ({sub_dir.upper()}) — {os.path.basename(root_dir)}',
#         fontsize=14
#     )
#     plt.xticks(rotation=90, ha='right', fontsize=9)
#     plt.yticks(fontsize=10)
#     plt.grid(axis='y', linestyle='--', alpha=0.7)

#     plt.tight_layout()

#     output_path = os.path.join(
#         save_folder, f'avg_frames_per_class_{sub_dir}.png'
#     )
#     plt.savefig(output_path, dpi=300)
#     plt.show()

#     print(f"{sub_dir} plot saved in {output_path}")
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# Paths
# --------------------------------------------------
root_dir = r"E:\Extra\shawon\BdSLW60 Full DataSet Version 2\Train-Test-Val(U1)-BdSLW60"
save_folder = r"C:\Users\shawo\Desktop\MSc New Exp Data"
os.makedirs(save_folder, exist_ok=True)
os.makedirs(save_folder, exist_ok=True)

sub_dirs = ['train', 'val', 'test']


# --------------------------------------------------
# Process each split
# --------------------------------------------------
for sub_dir in sub_dirs:
    sub_dir_path = os.path.join(root_dir, sub_dir)
    if not os.path.exists(sub_dir_path):
        print(f"Skipping missing directory: {sub_dir_path}")
        continue

    class_frame_lists = {}  # {class_name: [frame_counts]}

    # Iterate class folders
    for class_dir in os.listdir(sub_dir_path):
        class_path = os.path.join(sub_dir_path, class_dir)
        if not os.path.isdir(class_path):
            continue

        for file in os.listdir(class_path):
            if file.endswith('.mp4'):
                video_path = os.path.join(class_path, file)

                video = cv2.VideoCapture(video_path)
                if not video.isOpened():
                    continue

                frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
                video.release()

                class_frame_lists.setdefault(class_dir, []).append(frame_count)

    if not class_frame_lists:
        print(f"No videos found in {sub_dir}")
        continue

    # --------------------------------------------------
    # Compute statistics
    # --------------------------------------------------
    classes = sorted(class_frame_lists.keys())

    avg_frames = []
    class_sizes = []
    x_labels = []

    for cls in classes:
        frames = class_frame_lists[cls]
        avg_frames.append(np.mean(frames))
        class_sizes.append(len(frames))
        x_labels.append(f"{cls} ({len(frames)})")

    # --------------------------------------------------
    # Plot
    # --------------------------------------------------
    plt.figure(figsize=(16, 6))
    plt.bar(x_labels, avg_frames)
    plt.xlabel("Classes (Number of Samples)", fontsize=12)
    plt.ylabel("Average Frame Count", fontsize=12)
    plt.title(
        f"Average Frames per Class ({sub_dir.upper()}) — {os.path.basename(root_dir)}",
        fontsize=14
    )
    plt.xticks(rotation=90, ha='right', fontsize=9)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()

    output_path = os.path.join(
        save_folder, f"avg_frames_per_class_with_counts_{sub_dir}.png"
    )
    plt.savefig(output_path, dpi=300)
    plt.show()

    print(f"{sub_dir} plot saved in {output_path}")
