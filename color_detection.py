import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
from sklearn.cluster import KMeans
from scipy.spatial import KDTree

def nearest_color_name(center):
    colors = {
        "red": (255,0,0),
        "green": (0,255,0),
        "blue": (0,0,255),
        "yellow": (255,255,0)
    }
    dist_min = float("inf")
    nearest_color = None
    for color, value in colors.items():
        distance = sum([(i - j) ** 2 for i,j in zip(center, value)])
        if distance < dist_min:
            dist_min = distance
            nearest_color = color
    print(nearest_color)
    return nearest_color

def color_detection(image_file):
    image = cv2.imread(image_file)
    #plt.imshow(image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = image.reshape((image.shape[1]*image.shape[0], 3))

    color_classification = KMeans(n_clusters = 1)
    s = color_classification.fit(image)
    
    labels = color_classification.labels_
    labels = list(labels)
    print(labels)

    centroid = color_classification.cluster_centers_
    print(centroid)

    color = nearest_color_name(centroid)
    return color

def main():
    color = nearest_color_name(255,0,0)
    print(str(color))

if __name__ == "__main__":
    main()