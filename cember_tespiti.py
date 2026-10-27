import cv2
import numpy as np
import goruntu_ayarlari as g


cemberler=cv2.HoughCircles(
    g.blurlama,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=30,
    param1=50,
    param2=30,
    minRadius=10, 
    maxRadius=50
)

