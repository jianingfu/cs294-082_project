import cv2
import numpy as np
import os
import csv
import random

image_size = 224
path = "train 2"
ratio = 0.5
a = []
for f in os.listdir(path):
    if not f.startswith('.') and random.random() <= ratio:
        img = cv2.imread(os.path.join(path, f))
        img = cv2.resize(img, (image_size, image_size))
        arr = img.flatten().tolist()
        if f.startswith('c'):
            arr.append(0)
        else:
            arr.append(1)
        a.append(arr)

print(len(a))
print(len(a[3]))
with open("data2.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerows(a) 