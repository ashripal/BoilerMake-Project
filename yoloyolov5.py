import torch
from color_detection import color_detect, nearest_color_name
from PIL import Image
import numpy as np
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
    results = model(img)
    crops = results.crop(save = True)
    print(type(crops))
    array = np.array()
    im = Image.fromarray(crops)
    im.save("croppped.png")
    
    
    color_detect("cropped.png")