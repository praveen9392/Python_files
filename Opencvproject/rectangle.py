import cv2 as cv
img = cv.imread('Opencvproject/image.jpg')
draw=cv.rectangle(img,(100,100),(110,110),(255,0,0),1)
cv.imshow('imag', draw)
cv.waitKey(0)
cv.destroyAllWindows()