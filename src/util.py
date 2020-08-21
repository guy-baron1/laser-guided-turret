import cv2

def getOutermostContour(contours):
    if(len(contours) == 0):
        return
    outermost_contour = contours[0]
    for cnt in contours:
        if cv2.contourArea(cnt) > cv2.contourArea(outermost_contour):
            outermost_contour = cnt
    print (outermost_contour)
    return outermost_contour