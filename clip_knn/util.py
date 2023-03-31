import numpy
import torch
import clip
import numpy as np
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
import os

class Prediction():
    def __init__(self, desc, y):
        self.description = desc
        self.y = y

    def __str__(self):
        return self.description

class Model:
    def __init__(self, N, metric, train):
        self.train_path = train
        X, y = [], []
        self.knn = KNeighborsClassifier(N, metric=metric)
        self.knn.fit(X, y)

    def get_embeddings(self, filenames: list[str]) -> dict[str, np.array]:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model, preprocess = clip.load("ViT-B/32", device=device)
        images = {filename: preprocess(Image.open(filename)).unsqueeze(0).to(device) for filename in filenames}
        with torch.no_grad():
            images_embeds = {filename: model.encode_image(images[filename]).numpy()[0] for filename in filenames}
        return images_embeds

    def add_label_data(self, train_path, dr, knn_fit=False):
        y = []
        X = []
        img_paths = [img_path for img_path in os.listdir(train_path + '/' + dr) if '.txt' not in img_path]
        embs = get_embeddings(img_paths)
        for emb in embs:
            X.append(emb)
        y += [dr] * len(embs)
        self.X += X
        self.y += y
        if knn_fit:
            self.knn_fit()

    def get_train_data(self, train_path):
        for dr in os.listdir(train_path):
            add_label_data(train_path, dr)
        self.knn_fit()

    def fit(self):
        self.knn.fit(self.X, self.y)

    def merge(self, ls):
        out = []
        for l in ls:
            out += l
        return out

    def predict(self, to_predict_path):
        embs = self.get_embeddings([to_predict_path])
        p = self.knn([embs])
        with open(train_path + '/' + p + '/desc.txt', 'r') as f:
            desc = f.read().strip()
        return Prediction(desc, p)
        

if __name__ == "__main__":
    print(get_embeddings(["ClothesDataset/v2/1_0.jpg"]))
