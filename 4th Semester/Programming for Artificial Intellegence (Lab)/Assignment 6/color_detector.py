from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

def extract(image_path, k=5):
    image=Image.open(image_path)
    image=image.resize((150, 150))
    pixels=np.array(image).reshape(-1, 3)

    kmeans=KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)

    colors=kmeans.cluster_centers_.astype(int)
    hex_colors=[]
    for color in colors:
        r,g,b=color
        hex_code=f"#{r:02x}{g:02x}{b:02x}"
        hex_colors.append(hex_code)

    return hex_colors

