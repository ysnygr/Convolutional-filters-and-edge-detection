#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 08:19:39 2021

@author: yasin
"""

import cv2
import numpy as np
import glob

list_images = glob.glob("/home/yasin/Documents/Desktop/Work/Exercises/Convolutional_Edge_Detection/Images/*")

for image_title in list_images:
    img = cv2.imread(image_title,cv2.IMREAD_GRAYSCALE)

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    magnitude_spectrum = np.asarray(magnitude_spectrum, dtype = np.uint8)
    img_and_magnitude = np.concatenate((img,magnitude_spectrum),axis = 1)
    cv2.imshow(image_title,img_and_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()


    