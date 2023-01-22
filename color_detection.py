import numpy as np
import matplotlib.image as mp_img
import cv2
from sklearn.cluster import KMeans
import math

def nearest_color_name(center):
    colors = {
        #"red": (180,0,0),
        "green": (0,153,0),
        "blue": (51,153,255),
        "yellow": (200,200,50),
        "red": (153, 76, 0), 
        "black": (0, 0, 0), 
        "white": (255, 255, 255),
        "purple": (153, 51, 255)
    }
    dist_min = float("inf")
    color = None

    for color, value in colors.items():
        #print("center: {:d}\n", center)
        distance = math.dist(center, value)
        if (distance < dist_min):
            dist_min = distance
            nearest_color = color
    print(nearest_color)
    return nearest_color

def color_detect(image_file):
    #image = cv2.cvtColor(cv2.imread(image_file), cv2.COLOR_BGR2RGB)
    image = cv2.imread(image_file)
    #image_file = image_file[:,:,[2,1,0]]
    #image = mp_img.imread(image_file)

    row, col, channel = image.shape

    if channel == 4:
        rgb = np.zeros( (row, col, 3), dtype='float32' )
        r, g, b, a = image[:,:,0], image[:,:,1], image[:,:,2], image[:,:,3]

        a = np.asarray( a, dtype='float32' ) / 255.0

        R, G, B = (255,255,255)

        rgb[:,:,0] = r * a + (1.0 - a) * R
        rgb[:,:,1] = g * a + (1.0 - a) * G
        rgb[:,:,2] = b * a + (1.0 - a) * B
        image = np.asarray( rgb, dtype='uint8' )

    image = image.reshape((image.shape[1]*image.shape[0], 3))

    #finds most prominent color
    color_classification = KMeans(n_clusters = 1)
    color_classification.fit(image)
    
    labels = color_classification.labels_
    labels = list(labels)
    #print(labels)

    centroid = color_classification.cluster_centers_
    #print("tuple: {:s}", tuple(centroid.tolist()[0]))

    #gets color name from rgb value
    color = nearest_color_name(tuple(centroid.tolist()[0]))
    return color

def main():
    color_detect("apple_test.jpeg")
    color_detect("green_test.jpeg")
    color_detect("blue_test.jpg")
    color_detect("yellow_test.jpg")
    color_detect("20230121_145529.jpg")


if __name__ == "__main__":
    main()