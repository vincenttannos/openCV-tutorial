#!/usr/bin/env python3

import os
import cv2

# read image
image_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "Mob_psycho.jpg")
img = cv2.imread(image_path)

# resize
# print(img.shape)
img = cv2.resize(img, (340, 480))

# threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # values under 120 go to 0, over goes to 255
# ret, threshold = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)

# # to improve thresholding, can blur
# threshold = cv2.blur(threshold, (10, 10))
# ret, threshold = cv2.threshold(threshold, 120, 255, cv2.THRESH_BINARY)

############################################################################

# runs a kernel over it to find a good threshold
adaptive = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 30)

# visualise image
cv2.imshow('image', img)
cv2.imshow('gray', img_gray)
cv2.imshow('adaptive', adaptive)
# cv2.imshow('threshold', threshold)
cv2.waitKey(0) # 0 -> indefinite, 5000 -> open for 5000ms

# thresholding is good for removing shadows for OCR etc
