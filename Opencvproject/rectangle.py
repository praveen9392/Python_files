import cv2

# Load an image
img = cv2.imread('Opencvproject/image.jpg')

# Draw a bounding box around an object
cv2.rectangle(img, (70, 50), (150, 150), (0, 255, 0), 2)

# Display the output
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

