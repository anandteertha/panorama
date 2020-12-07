import cv2
import numpy as np


dim = (700,700)
left = cv2.imread('pic1.png',cv2.IMREAD_COLOR)
left = cv2.resize(left,dim,interpolation = cv2.INTER_AREA)

right = cv2.imread('pic2.png',cv2.IMREAD_COLOR)
right = cv2.resize(right,dim,interpolation = cv2.INTER_AREA)

images = []
images.append(left)
images.append(right)

sticher = cv2.Stitcher.create()
ret, pano = sticher.stitch(images)

if ret == cv2.STITCHER_OK:
    cv2.imshow('panaroma',pano)
    cv2.waitKey()
    cv2.destroyAllWindows()

else:
    print('error during stitching')

cv2.waitKey(0)
cv2.destroyAllWindows()








cv2.waitKey(0)
cv2.destroyAllWindows()
