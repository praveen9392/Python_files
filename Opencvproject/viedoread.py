import cv2 as cv

viedo = cv.VideoCapture('C:/Users/PRAVEEN/Videos/problem.mp4')
while True:
    true, frame = viedo.read()
    cv.imshow('frame', frame)

capture.relaese()
cv.waitKey(0)