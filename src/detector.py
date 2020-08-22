import cv2
import numpy as np
import time
from util import getOutermostContour

 
#cap = cv2.VideoCapture('../data/laser.mp4')
cap = cv2.VideoCapture(0)
while 1: 
 
    ret, img = cap.read()
    if not ret:
        break

    # convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #lower/upper hsv limits
    lower_limit = np.array([65, 40, 215])
    upper_limit = np.array([100, 50, 255])

    #get threshold mask
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    #remove noise (erosion => dilation)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # find contours in mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draw outermost contour
    if len(contours) > 0:
        outer_contour = getOutermostContour(contours)
        x,y,w,h = cv2.boundingRect(outer_contour)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    
    cv2.imshow('mask',mask)
    cv2.imshow('raw', img)
 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
cap.release()

cv2.destroyAllWindows() 
