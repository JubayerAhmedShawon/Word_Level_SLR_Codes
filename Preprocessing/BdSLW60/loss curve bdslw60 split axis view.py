import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# -----------------------------
# Load trainer_state.json
# -----------------------------
path = r"C:\Users\shawo\Desktop\revision\new figures\trainer_state.json"


with open(path, "r") as f:
    data = json.load(f)

logs = data["log_history"]

train_steps, train_loss = [], []
val_steps, val_loss = [], []

for entry in logs:
    if "loss" in entry and "step" in entry:
        train_steps.append(entry["step"])
        train_loss.append(entry["loss"])
    if "eval_loss" in entry and "step" in entry:
        val_steps.append(entry["step"])
        val_loss.append(entry["eval_loss"])

train_steps = np.array(train_steps)
train_loss = np.array(train_loss)
val_steps = np.array(val_steps)
val_loss = np.array(val_loss)

# ========================= PLOS ONE Figure Defaults =========================
plt.rcParams.update({
    "font.size": 10,          # Minimum PLOS requirement
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "lines.linewidth": 1.5,   # PLOS minimum stroke width
})

# ========================= Split-Axis Plot =========================
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(5.5, 6), dpi=300,   # PLOS max width = 6.5 inches
    sharex=True, gridspec_kw={'height_ratios': [1, 3]}
)

# ----------------------- TOP AXIS (spike) -----------------------
ax1.plot(train_steps, train_loss, "-o", color="orange", label="Training Loss", markersize=4)
ax1.plot(val_steps, val_loss, "-o", color="red", label="Validation Loss", markersize=4)

ax1.set_ylim(train_loss.max() - 0.5, train_loss.max() + 0.1)
ax1.spines['bottom'].set_visible(False)
ax1.tick_params(labelbottom=False)

# ----------------------- BOTTOM AXIS (zoom) ----------------------
ax2.plot(train_steps, train_loss, "-o", color="orange", markersize=4)
ax2.plot(val_steps, val_loss, "-o", color="red", markersize=4)

ax2.set_ylim(0, max(train_loss[1:].max(), val_loss.max()) + 0.05)
ax2.spines['top'].set_visible(False)

# ----------------------- Broken Axis Indicators -------------------
d = .015  
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False, linewidth=1.2)
ax1.plot((-d, +d), (-d, +d), **kwargs)
ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)

kwargs = dict(transform=ax2.transAxes, color='k', clip_on=False, linewidth=1.2)
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

# ----------------------- Labels ------------------------
fig.suptitle("Loss Curve With Spike (Split-Axis View) - BdSLW60", fontsize=11)
ax2.set_xlabel("Training Steps")
ax2.set_ylabel("Loss")
ax1.legend(loc="upper right")

plt.tight_layout()

# =====================================================
#            PLOS ONE-Compliant TIFF Export
# =====================================================

# Step 1 — Save temporary PNG at very high DPI
png_path = "loss_split_axis_tmp.png"
plt.savefig(png_path, dpi=600, transparent=False)
plt.close()

# Step 2 — Convert PNG → TIFF while preserving DPI
tif_path = r"C:\Users\shawo\Desktop\revision\new figures\loss_split_axis_plos_one.tiff"
img = Image.open(png_path).convert("RGB")
img.save(tif_path, compression="tiff_lzw", dpi=(300, 300))

print("PLOS ONE TIFF Saved:", tif_path)
