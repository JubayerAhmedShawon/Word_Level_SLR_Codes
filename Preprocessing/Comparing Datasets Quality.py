import cv2
import numpy as np
import pandas as pd
import os

# ================== Quality Metrics ==================

def sharpness_score(frame):
    return cv2.Laplacian(frame, cv2.CV_64F).var()

def brightness_score(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray.mean()

def contrast_score(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray.std()

def noise_score(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    median = cv2.medianBlur(gray, 5)
    return np.mean(np.abs(gray - median))

def blockiness_score(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h_diff = np.sum(np.abs(np.diff(gray, axis=1)))
    v_diff = np.sum(np.abs(np.diff(gray, axis=0)))
    return (h_diff + v_diff) / gray.size

# ================== Uniform Sampling ==================

def extract_uniform_frames(video_path, num_frames=5):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"❌ Cannot open: {video_path}")
        return []

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames <= 1:
        print(f"❌ Not enough frames: {video_path}")
        return []

    # pick frames at 10%, 30%, 50%, 70%, 90%
    positions = np.linspace(0.1, 0.9, num_frames)
    selected_frames = []

    for p in positions:
        frame_id = int(p * total_frames)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = cap.read()
        if ret:
            selected_frames.append(frame)

    cap.release()
    return selected_frames

# ================== Analyze Single Video ==================

def analyze_video(dataset_name, video_path):
    frames = extract_uniform_frames(video_path, num_frames=5)

    if len(frames) == 0:
        return None

    sharp = []
    bright = []
    contrast = []
    noise = []
    block = []

    for f in frames:
        sharp.append(sharpness_score(f))
        bright.append(brightness_score(f))
        contrast.append(contrast_score(f))
        noise.append(noise_score(f))
        block.append(blockiness_score(f))

    return {
        "dataset": dataset_name,
        "video": os.path.basename(video_path),
        "sharpness": np.mean(sharp),
        "brightness": np.mean(bright),
        "contrast": np.mean(contrast),
        "noise": np.mean(noise),
        "blockiness": np.mean(block)
    }

# ================== Your Video Paths ==================

videos = {
    "wlasl": r"BdSLW60_10_Fold/quality check/63225.mp4",
    "bdslw": r"BdSLW60_10_Fold/quality check/U1W41F_trial_1_L.mp4",
    "lsa64": r"BdSLW60_10_Fold/quality check/002_003_001.mp4"
}

# ================== Run & Save ==================

results = []

for name, path in videos.items():
    print(f"Processing {name}...")
    metrics = analyze_video(name, path)
    if metrics:
        results.append(metrics)

df = pd.DataFrame(results)
df.to_csv(r"BdSLW60_10_Fold/quality check/uniform5_dataset_quality.csv", index=False)

print("\nSaved: uniform5_dataset_quality.csv")
print(df)
