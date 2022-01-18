#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 06:01:20 2021

@author: yasin
"""

import cv2
import numpy as np



img = cv2.imread("/home/yasin/Documents/Desktop/Work/Exercises/Image_Representations/day_night_images/training/day/20151102_121045.jpg")

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 5)

gaussian_blur  = cv2.GaussianBlur(img,(5,5),0)



cv2.imshow("img-real",img)
cv2.imshow("img",gaussian_blur)   
cv2.waitKey(0)
cv2.destroyAllWindows()