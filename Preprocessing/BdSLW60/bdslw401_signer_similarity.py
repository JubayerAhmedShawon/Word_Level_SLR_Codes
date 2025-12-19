import os
import re
import pandas as pd
import matplotlib.pyplot as plt
s
# ----------------------------------------------
# 1. Regex pattern for new MP4 convention
#    Format: W001S04F_02.mp4
# ----------------------------------------------

pattern = re.compile(r"(W\d{3})S(\d{2})F")

# ----------------------------------------------
# 2. Load dataset: read train/val/test structure
# ----------------------------------------------

def load_dataset(root):
    records = []

    for split in ["train", "val", "test"]:
        split_path = os.path.join(root, split)
        if not os.path.isdir(split_path):
            continue

        for cls_folder in os.listdir(split_path):
            cls_path = os.path.join(split_path, cls_folder)
            if not os.path.isdir(cls_path):
                continue

            for f in os.listdir(cls_path):
                m = pattern.search(f)
                if not m:
                    continue

                class_id = m.group(1)          # W001
                signer = "S" + m.group(2)      # S04

                records.append([split, class_id, signer])

    return pd.DataFrame(records, columns=["split", "class", "signer"])


# ----------------------------------------------
# 3. Compute same-signer vs different-signer %
# ----------------------------------------------

def compute_signer_similarity(df):
    classes = sorted(df["class"].unique(), key=lambda x: int(x[1:]))

    results = []
    for c1, c2 in zip(classes[:-1], classes[1:]):
        signers1 = set(df[df["class"] == c1]["signer"])
        signers2 = set(df[df["class"] == c2]["signer"])

        same = len(signers1.intersection(signers2))
        diff = len(signers1.union(signers2)) - same

        total = same + diff
        same_pct = (same / total * 100) if total > 0 else 0
        diff_pct = (diff / total * 100) if total > 0 else 0

        results.append([f"{c1}-{c2}", same_pct, diff_pct])

    return pd.DataFrame(results, columns=["class_pair", "same_pct", "diff_pct"])


# ----------------------------------------------
# 4. Plot (PLOS version)
# ----------------------------------------------
save_path = r"/media/cse/HDD/Shawon/shawon/BdSLW60_10_Fold/signer_similarity_bdslw401.tiff"


def plot_similarity_plos(df_pairs, tick_interval=30, save_path=None):
    if df_pairs.empty:
        print("No data to plot.")
        return

    indices = list(range(len(df_pairs)))

    fig_width = min(12, max(6, len(df_pairs) / 50))
    fig_height = 5
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.bar(indices, df_pairs["same_pct"], label="Same Signer", color="#1f77b4")
    ax.bar(indices, df_pairs["diff_pct"], bottom=df_pairs["same_pct"],
           label="Different Signer", color="#ff7f0e")

    ax.set_ylabel("Percentage (%)", fontsize=10, fontname='Arial')
    ax.set_xlabel("Adjacent Class Pairs", fontsize=10, fontname='Arial')
    ax.set_title("Percentage of Same vs Different Signers per Class (BdSLW401)",
                 fontsize=10, fontname='Arial')

    tick_positions = [0] + list(indices[tick_interval::tick_interval])
    if indices[-1] not in tick_positions:
        tick_positions.append(indices[-1])

    tick_labels = [df_pairs["class_pair"].iloc[i] for i in tick_positions]

    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels, rotation=45, ha='right', fontsize=7, fontname='Arial')

    ax.legend(fontsize=10)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, format='tiff', dpi=300)
        print(f"Figure saved to {save_path}")
    else:
        plt.show()

    plt.close(fig)


# ----------------------------------------------
# 5. RUN EVERYTHING
# ----------------------------------------------

if __name__ == "__main__":
    root = r"MY DATA/BdSLW401"  
    

    df = load_dataset(root)
    print("Loaded dataset:")
    print(df.head())

    df_pairs = compute_signer_similarity(df)
    print("\nSigner similarity per adjacent class pair:")
    print(df_pairs.head())

plot_similarity_plos(df_pairs, tick_interval=30, save_path=save_path)
