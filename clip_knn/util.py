import numpy
import torch
import clip
import numpy as np
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
import os
import base64
from sklearn.exceptions import NotFittedError


class Prediction():
    def __init__(self, desc, y):
        self.description = desc
        self.y = y

    def __str__(self):
        return self.description


class Model:
    def __init__(self, N, metric, train):
        self.train_path = train
        self.X, self.y = [], []
        self.knn = KNeighborsClassifier(N, metric=metric)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=device)
        # self.knn.fit(X, y)

    def get_embeddings(self, filenames: list[str]) -> dict[str, np.array]:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        images = {filename: self.preprocess(Image.open(filename)).unsqueeze(0).to(device) for filename in filenames}
        with torch.no_grad():
            images_embeds = {filename: self.model.encode_image(images[filename]).numpy()[0] for filename in filenames}
        return images_embeds

    def add_label_data(self, train_path, dr, knn_fit=False):
        y = []
        X = []
        img_paths = [f"{train_path}/{dr}/{img_path}" for img_path in os.listdir(train_path + '/' + dr) if '.txt' not in img_path]
        embs = self.get_embeddings(img_paths).values()
        for emb in embs:
            X.append(emb)
        y += [dr] * len(embs)
        self.X += X
        self.y += y
        if knn_fit:
            self.knn_fit()

    def get_train_data(self, train_path):
        for dr in os.listdir(train_path):
            self.add_label_data(train_path, dr)
        self.knn_fit()

    def knn_fit(self):
        self.knn.fit(self.X, self.y)

    def merge(self, ls):
        out = []
        for l in ls:
            out += l
        return out

    def predict(self, to_predict_path):
        embs = list(self.get_embeddings([to_predict_path]).values())[0]
        print(embs.shape)
        try:
            p = self.knn.predict([embs])
        except NotFittedError as e:

            self.get_train_data(self.train_path)
            p = self.knn.predict([embs])
        with open(self.train_path + '/' + p[0] + '/desc.txt', 'r') as f:
            desc = f.read().strip()
        return Prediction(desc, p)


class Database:
    def __init__(self, path):
        self.path = path
        self.model = Model(1, "cosine", self.path)
        self.label_counter = self.init_counter()

    def init_counter(self):
        labels = [int(x) for x in os.listdir(self.path)]
        if len(labels) > 0:
            return max(labels)
        return 0

    def get_category_label(self, category):
        for label in os.listdir(self.path):
            with open(f"{self.path}/{label}/desc.txt", "r") as f:
                if f.read() == category: return label
        return self.create_category(category)

    def create_category(self, category) -> str:
        self.label_counter += 1
        os.mkdir(f"{self.path}/{self.label_counter}")
        with open(f"{self.path}/{self.label_counter}/desc.txt", "w") as f:
            f.write(category)
        return str(self.label_counter)
    
    def get_category_counter(self, label):
        return len(os.listdir(f"{self.path}/{label}"))

    def add_to_category(self, label, b64_data):
        category_counter = self.get_category_counter(label)
        with open(f"{self.path}/{label}/{category_counter}.jpg", "wb") as f:
            f.write(base64.b64decode(b64_data))
        self.model.add_label_data(self.path, label, True)


if __name__ == "__main__":
    print(get_embeddings(["ClothesDataset/v2/1_0.jpg"]))
