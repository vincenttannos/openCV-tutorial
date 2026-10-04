#!/usr/bin/env python3

import os
import cv2

# read image
image_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "simplified.png")
img = cv2.imread(image_path)

# resize
img = cv2.resize(img, (352, 500))

# opencv uses BGR colourspace - B first, then G, then R
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# visualise image
cv2.imshow('image', img)
# cv2.imshow('RGB', img_rgb)
# cv2.imshow('gray', img_gray)
cv2.imshow('HSV', img_hsv)
cv2.waitKey(0) # 0 -> indefinite, 5000 -> open for 5000ms


