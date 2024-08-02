# Import the OpenCV library and assign it the alias 'cv'
import cv2 as cv

# Read an image from the file 'Opencvproject/image.jpg'
img = cv.imread('Opencvproject/image.jpg')

# Resize the image to a width of 800 pixels and a height of 100 pixels
resize = cv.resize(img, (800, 1000))

# Display the resized image with the title 'imag'
cv.imshow('imag', resize)

# Wait for a key press, allowing the user to view the image before it closes
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()