import cv2
from sklearn.cluster import KMeans

def nearest_color_name(center):
    colors = {
        "red": (255,0,0),
        "green": (0,255,0),
        "blue": (0,0,255),
        "yellow": (255,255,0),
        "black": (0,0,0),
        "white": (255,255,255),
        "grey": (128,128,128),
        "purple": (128,0,128),
        "pink": (255,105,180),
        "orange": (255,140,0),
        "brown": (165,42,42)
    }
    dist_min = float("inf")
    for color, value in colors.items():
        distance = sum([(c - v) ** 2 for c,v in zip(center, value)])
        if distance < dist_min:
            dist_min = distance
            nearest_color = color
    print(nearest_color)
    return nearest_color

def color_detection(image_file):
    image = cv2.cvtColor(cv2.imread(image_file), cv2.COLOR_BGR2RGB)

    image = image.reshape((image.shape[1]*image.shape[0], 3))

    #finds most prominent color
    color_classification = KMeans(n_clusters = 1)
    color_classification.fit(image)
    
    labels = color_classification.labels_
    labels = list(labels)
    print(labels)

    centroid = color_classification.cluster_centers_
    print(tuple(centroid))

    #gets color name from rgb value
    color = nearest_color_name(tuple(centroid))
    return color

def main():
    color = nearest_color_name(((255,255,0)))
    print(str(color))

if __name__ == "__main__":
    main()