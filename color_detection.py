import numpy as np
import matplotlib.image as mp_img
import cv2
from sklearn.cluster import KMeans
import math

def nearest_color_name(center):
    colors = {
        "red": (255,0,0),
        "green": (0,255,0),
        "blue": (0,0,255),
        "yellow": (0,255,255)
    }
    dist_min = float("inf")
    color = None

    for color, value in colors.items():
        distance = math.dist(center, value)
        if (distance < dist_min):
            dist_min = distance
            nearest_color = color
    print(nearest_color)
    return nearest_color

def color_detection(image_file):
    image = cv2.cvtColor(cv2.imread(image_file), cv2.COLOR_BGR2RGB)
    #image_file = image_file[:,:,[2,1,0]]
    #image = mp_img.imread(image_file)

    #image = image.reshape((image.shape[1]*image.shape[0], 3))

    row, col, channel = image_file.shape

    if channel == 4:
        rgb = np.zeros( (row, col, 3), dtype='float32' )
        r, g, b, a = image_file[:,:,0], image_file[:,:,1], image_file[:,:,2], image_file[:,:,3]

        a = np.asarray( a, dtype='float32' ) / 255.0

        R, G, B = (255,255,255)

        rgb[:,:,0] = r * a + (1.0 - a) * R
        rgb[:,:,1] = g * a + (1.0 - a) * G
        rgb[:,:,2] = b * a + (1.0 - a) * B
        image_file = np.asarray( rgb, dtype='uint8' )

    #finds most prominent color
    color_classification = KMeans(n_clusters = 1)
    color_classification.fit(image)
    
    labels = color_classification.labels_
    labels = list(labels)
    #print(labels)

    centroid = color_classification.cluster_centers_
    #print(tuple(centroid))

    #gets color name from rgb value
    color = nearest_color_name(tuple(centroid))
    return color

def main():
    color = nearest_color_name(((0,255,255)))
    #print(str(color))
    color_detection("apple_test.jpeg")
    color_detection("orange_test.jpeg")
    color_detection("green_test.jpeg")
    color_detection('blue_test.jpeg')

if __name__ == "__main__":
    main()