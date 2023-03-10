# sudo apt install libgdal-dev
# pip install gdal==3.4.1

import os
import cv2
import numpy as np
from osgeo import gdal
from tqdm import tqdm

IMG_PATH = 'img/'
IMG_RESIZE_PATH = 'img_resize/'

img_file_list = []
for node_name in os.listdir(IMG_PATH):
    node_path = os.path.join(IMG_PATH, node_name)
    if os.path.isfile(node_path):
        img_file_list.append(node_name)

print(img_file_list)

pbar = tqdm(img_file_list)

for img_file in pbar:
    source = gdal.Open(IMG_PATH + img_file)

    red = source.GetRasterBand(3).ReadAsArray()
    green = source.GetRasterBand(2).ReadAsArray()
    blue = source.GetRasterBand(1).ReadAsArray()

    img_np = np.dstack((red, green, blue))
    # print(img_np.shape)

    resize_scale = 10
    new_size = (int(img_np.shape[1]/resize_scale),
                int(img_np.shape[0]/resize_scale))
    # print(new_size)

    img_resize_np = cv2.resize(img_np, new_size)
    # print(img_resize_np.shape)

    cv2.imwrite(IMG_RESIZE_PATH + img_file.split('.')
                [0] + '_resize_' + str(resize_scale) + '.bmp', img_resize_np)
