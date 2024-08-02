import cv2

# Read the image from file
image = cv2.imread(r'Opencvproject\image.jpg')

# Check if the image is loaded properly
if image is not None:
    # Draw the line
    cv2.line(image, (50, 50), (100, 100), (255, 0, 0), 2)

    # Save the image
    cv2.imwrite('line_image.jpg', image)

    # Display the image
    cv2.imshow('Image with Line', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load image.")
