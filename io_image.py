#!/usr/bin/env python3

import os
import cv2

# # read image
# image_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "simplified.png")

# img = cv2.imread(image_path)

# # write image
# cv2.imwrite(os.path.join("/mnt/c/Users/Vincent/Downloads/", "simplified1.png"), img)

# # visualise image
# cv2.imshow('image', img)
# cv2.waitKey(0) # 0 -> indefinite, 5000 -> open for 5000ms

################################################################################

# # read video
# video_path = os.path.join("/mnt/c/Users/Vincent/Downloads/", "render.mp4")

# video = cv2.VideoCapture(video_path)

# # visualise video
# ret = True
# while ret:
#     ret, frame = video.read() # ret is true when there's a new frame and false when there isn't

#     if ret:
#         cv2.imshow('frame', frame)
#         cv2.waitKey(1000//60) # frame rate

# # release memory
# video.release()
# cv2.destroyAllWindows()

################################################################################

# open powershell as admin and put in 'usbipd list'
# usbipd attach --wsl --busid <YOUR_BUS_ID>

# read webcam
webcam = cv2.VideoCapture(0) # stream 1 - webcam
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# change pixel format since wsl will drop packets otherwise - green screen
webcam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
# webcam.set(cv2.CAP_PROP_FPS, 30)

# visualise webcam
while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): # close window when press q
        break

webcam.release()
cv2.destroyAllWindows()

