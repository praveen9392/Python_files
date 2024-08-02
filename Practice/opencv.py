import cv2
import dlib

print("OpenCV version:", cv2.__version__)

# Initialize the facial landmark detection model
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:/Path/To/shape_predictor_68_face_landmarks.dat")# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame from camera")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray, 0)

    # Loop through each face
    for face in faces:
        # Detect facial landmarks
        landmarks = predictor(gray, face)

        # Loop through each facial landmark
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

    # Display the output
    cv2.imshow("Facial Landmarks", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()