import cv2
from sklearn.cluster import KMeans
import numpy as np

def extract(image_path, k=5):
    image=cv2.imread(image_path)
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image=cv2.resize(image, (150, 150))
    pixels=image.reshape(-1, 3)
    kmeans=KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    colors=kmeans.cluster_centers_.astype(int)
    hex_colors=[]
    for r,g,b in colors:
        hex_code=f"#{r:02x}{g:02x}{b:02x}"
        hex_colors.append(hex_code)
    return hex_colors
