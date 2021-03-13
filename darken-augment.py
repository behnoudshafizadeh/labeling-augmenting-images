#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def imageFilesIn(path: str):
    files = os.listdir(path)
    files = list(filter(lambda x: not os.path.isdir(os.path.join(path, x)), files))
    return list(filter(lambda x: x.split('.')[1]=="jpg", files))
    


# In[ ]:


def makedarkImageFrom(image_path):
    dummy_name = 'dark'
    file_name = os.path.basename(image_path).split('.')[0]
    directory_path = os.path.dirname(image_path)
    
    old_image_name = file_name + '.jpg'
    new_image_name = file_name +dummy_name + '.jpg'
    old_image_path = os.path.join(directory_path, old_image_name)
    x='dark'
    directory_path = os.path.join(directory_path,x)
    new_image_path = os.path.join(directory_path, new_image_name)
    
    
    image = mpimg.imread(old_image_path)
    darkimage = am.darken(image, darkness_coeff= 0.8) 
    mpimg.imsave(new_image_path, darkimage)
    


# In[ ]:


import os
import Automold as am
import Helpers as hp
import cv2
import PIL
from PIL import Image
import matplotlib.image as mpimg
import math
from PIL import Image,ImageFilter
from bs4 import BeautifulStoneSoup, Tag, NavigableString


main_path = '/home/user/anaconda3/imgaug-master/dataset6661jpeg'

jpeg_files = imageFilesIn(main_path)
for image_file_name in jpeg_files:
    image_path = os.path.join(main_path, image_file_name)
    makedarkImageFrom(image_path)


# In[ ]:





# In[ ]:




