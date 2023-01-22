import torch
from color_detection import color_detect, nearest_color_name
from PIL import Image
import numpy as np
import os
# Model
def yoloyolov5(filename):
    '''
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, etc.
    # model = torch.hub.load('ultralytics/yolov5', 'custom', 'path/to/best.pt')  # custom trained model

    # Images
    im = filename  # or file, Path, URL, PIL, OpenCV, numpy, list

    # Inference
    results = model(im)

    # Results
    results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

    results.xyxy[0]  # im predictions (tensor)
    results.pandas().xyxy[0]  # im predictions (pandas)
    '''

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    img = filename
    #print(filename)
    results = model(img)
    crops = results.crop(save = True)
    #print(crops)
    d = {}
    for i in range(len(crops)):
        
        img = Image.fromarray(crops[i]['im'])
        img.save(f"file{i}.jpeg")
        #d[i].value = color_detect(f"file{i}.jpeg")
        d[crops[i]['label']]  = color_detect(f"file{i}.jpeg")

    #print(crops['label'])
    #print('File name: ', os.path.basename(__file__))
    #print('Directory name: ', os.path.dirname(__file__))
   
    return d

   
    
    #color_detect("runs\detect\exp\crops\imageCap.jpg")