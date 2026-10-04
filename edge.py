#!/usr/bin/env python3

import os
import cv2
import numpy as np

# read image
image_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "Mob_psycho.jpg")
img = cv2.imread(image_path)

# resize
# print(img.shape)
# img = cv2.resize(img, (340, 480))

# edge detection
# openCV has documentation of how it works
img_edge = cv2.Canny(img, 100, 200)

# np.ones creates a numpy array 
# dilate() makes a thicker line
img_dilate = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))

img_erode = cv2.erode(img_dilate, np.ones((3, 3), dtype=np.int8))

# visualise image
cv2.imshow('image', img)
cv2.imshow('canny', img_edge)
cv2.imshow('dilated', img_dilate)
cv2.imshow('erode', img_erode)
cv2.waitKey(0) # 0 -> indefinite, 5000 -> open for 5000ms

# thresholding is good for removing shadows for OCR etc
