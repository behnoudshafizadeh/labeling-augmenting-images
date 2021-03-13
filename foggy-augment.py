#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def imageFilesIn(path: str):
    files = os.listdir(path)
    files = list(filter(lambda x: not os.path.isdir(os.path.join(path, x)), files))
    return list(filter(lambda x: x.split('.')[1]=="jpg", files))
    


# In[ ]:


def makefoggyImageFrom(image_path):
    dummy_name = 'foggy'
    file_name = os.path.basename(image_path).split('.')[0]
    directory_path = os.path.dirname(image_path)
    
    old_image_name = file_name + '.jpg'
    new_image_name = file_name +dummy_name + '.jpg'
    old_image_path = os.path.join(directory_path, old_image_name)
    x='foggy'
    directory_path = os.path.join(directory_path,x)
    new_image_path = os.path.join(directory_path, new_image_name)
    
    
    image = imageio.imread(old_image_path)
    foggyimage = aug.augment_image(image)
    cv2.imwrite(new_image_path,foggyimage)
 
    


# In[ ]:


import os
import cv2
import PIL
from PIL import Image
import matplotlib.image as mpimg
import math
from PIL import Image,ImageFilter
from bs4 import BeautifulStoneSoup, Tag, NavigableString
import imageio
import imgaug as ia
from imgaug import augmenters as iaa

main_path = '/home/user/anaconda3/imgaug-master/dataset6661jpeg'
#size of snowflakes
aug =  iaa.Fog()
jpeg_files = imageFilesIn(main_path)
for image_file_name in jpeg_files:
    image_path = os.path.join(main_path, image_file_name)
    makefoggyImageFrom(image_path)


# In[ ]:




