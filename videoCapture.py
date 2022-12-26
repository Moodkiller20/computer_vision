"""
    Video capture with python and OpenCv2

"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # To connect to  your camera.

# un comment this line if you have a video file.
# cap = cv2.VideoCapture("PATH TO YOUR VIDEO FILE")

# This will go until with press a key to quit the program.
while True:
    """
    *   ret is a boolean variable that returns true if the frame is available. So let say if You only have one camera 
        and that camera is already being used by anther software, ret will return False
        
    *   frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
    """
    ret, frame = cap.read()

    # imshow takes in the frame title and the frame value return by the above line and display
    cv2.imshow('Frame Title', frame)

    # Wait for 10 millisecond and if in that x millisecond you press 'q' it will break out of the loop.
    if cv2.waitKey(10) == ord('q'):
        break

# This release the camera resources so a another program can use it.
cap.release()

cv2.destroyAllWindows()
