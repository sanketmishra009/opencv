import cv2 as cv
import numpy as np

def rescaleImage(frame , scale = 0.75):

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimentions = (width, height)

    return cv.resize(frame , dimentions , interpolation = cv.INTER_AREA)


capture = cv.VideoCapture('../../videos/hero.mov')

isTrue , Frame = capture.read()
while(isTrue):
    cv.imshow('Original Video' , Frame)
    cv.imshow('Rescaled Video', rescaleImage(Frame , 0.2))
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    isTrue , Frame = capture.read()

capture.release()
cv.destroyAllWindows()