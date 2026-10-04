#!/usr/bin/env python3

import os
import cv2

# read image
image_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "simplified.png")
img = cv2.imread(image_path)

# resize
img = cv2.resize(img, (352, 500))

# blur - removes noise
"""
blur()
gaussianBlur()
medianBlur()
bilateralFilter()
"""
k_size = 15 # kernel size
blurred_img = cv2.blur(img, (k_size, k_size)) # box blur
gaussian_img = cv2.GaussianBlur(img, (k_size, k_size), 3)
median = cv2.medianBlur(img, k_size) # keeps sharp edges - takes median pixel of kernel

# visualise image
cv2.imshow('image', img)
cv2.imshow('blur', blurred_img)
cv2.imshow('gaussian', gaussian_img)
cv2.imshow('median', median)
cv2.waitKey(0) # 0 -> indefinite, 5000 -> open for 5000ms


