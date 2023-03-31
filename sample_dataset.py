import os

import clip_knn.util as utils

for filename in os.listdir("ClothesDataset/v2"):
    if not filename.endswith(".jpg"): continue
    label, idx = filename.strip().split("_")