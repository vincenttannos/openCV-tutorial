#!/usr/bin/env python3

import os
import cv2

# read image
image_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "simplified.png")
img = cv2.imread(image_path)

# (height, width, channels) - rows, columns, channels
print(img.shape)

# slices of the numpy array
# you can take the pixels by hovering a mouse over the imshow of og pic
cropped_img = img[320:640, 420:840]

# visualise image
cv2.imshow('image', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0) # 0 -> indefinite, 5000 -> open for 5000ms


