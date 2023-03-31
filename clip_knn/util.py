import numpy
import torch
import clip
import numpy as np
from PIL import Image


def get_embeddings(filenames: list[str]) -> dict[str, np.array]:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)

    images = {filename: preprocess(Image.open(filename)).unsqueeze(0).to(device) for filename in filenames}

    with torch.no_grad():
        images_embeds = {filename: model.encode_image(images[filename]).numpy()[0] for filename in filenames}

    return images_embeds


if __name__ == "__main__":
    print(get_embeddings(["ClothesDataset/v2/1_0.jpg"]))
