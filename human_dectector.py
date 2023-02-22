import cv2
import datetime

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles and labels around the faces
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Human', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            print("Human detected at (x, y) = ({}, {}) at time {}".format(x, y, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    else:
        print("No human has been detected at time {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # Display the frame
    cv2.imshow('Camera', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
