
import matplotlib.pyplot as plt
from PIL import Image

fig, axes = plt.subplots(2, 2, figsize=(14, 18))

volumes = [
    ("cover_volume1.png", "Volume 1 (Green)"),
    ("cover_volume2.png", "Volume 2 (Blue)"),
    ("cover_volume3.png", "Volume 3 (Purple)"),
    ("cover_volume4.png", "Volume 4 (Brown/Orange)"),
]

for idx, (filename, title) in enumerate(volumes):
    row, col = idx // 2, idx % 2
    img = Image.open(f"/mnt/agents/output/{filename}")
    axes[row, col].imshow(img)
    axes[row, col].axis('off')
    axes[row, col].set_title(title, fontsize=14)

plt.tight_layout()
plt.savefig("/mnt/agents/output/preview_all_volumes_correct.png", dpi=150, bbox_inches='tight')
plt.show()
