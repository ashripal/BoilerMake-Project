# import required modules
import torch
from IPython.display import Image  # for displaying images
import os 
import random
import shutil
from sklearn.model_selection import train_test_split
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tqdm import tqdm
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import zipfile

random.seed(108)

# function below crops individual bounding boxes in image input
def crop_img(path):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    img = path
    results = model(img)
    crops = results.crop(save = True)
    print(type(crops))
    return crops

def img_color(list_crops):
    


