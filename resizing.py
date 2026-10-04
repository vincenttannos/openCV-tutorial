#!/usr/bin/env python3

import os
import cv2

# read image
image_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "simplified.png")
img = cv2.imread(image_path)

# (width, height)
resized_img = cv2.resize(img, (640,480))

# (height, width, channels) - rows, columns, channels
print(img.shape)

# visualise image
cv2.imshow('image', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0) # 0 -> indefinite, 5000 -> open for 5000ms


