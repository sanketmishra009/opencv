import cv2 as cv
import numpy as np

capture = cv.VideoCapture('../../videos/hero.mov')

isTrue , Frame = capture.read()
while(isTrue):
    cv.imshow('Video', Frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    isTrue , Frame = capture.read()

capture.release()
cv.destroyAllWindows()