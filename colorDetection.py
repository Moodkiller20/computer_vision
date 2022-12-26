"""
    Color detection.
    This program detect takes HSV color input value to extract from an image or video. The inout color will be shown on the screen and everything else
    outside the range will be in black.
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # To connect to  your camera.

# uncomment this line if you have a video file.
# cap = cv2.VideoCapture("PATH TO YOUR VIDEO FILE")

# This will go until with press a key to quit the program.
while True:
    """
    *   ret is a boolean variable that returns true if the frame is available. So let say if You only have one camera 
        and that camera is already being used by anther software, ret will return False

    *   frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
    """
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    """
    Colors Representation
    RGB: Red, Green & blue 
    BGR: Blue, Green & Red
    HSV: Hue, Saturation & Lightness/Brightness
    """

    # Converting BGR to HSV image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Extract colors
    lower_blue = np.array([90, 50, 50])  # Light blue
    upper_blue = np.array([130, 255, 255])  # Dark blue

    # create a mask, a mask is like a portion or part of an image.
    mask = cv2.inRange(hsv, lower_blue,
                       upper_blue)  # This return only the pixel withing the range of colors defined in the parameters

    """
    bitwise_and : Takes in two frame merges them and and compares them using the mask, any pixels that matches the mask will be dislpayed  in colors
    and anything else will be turned into black.
    bitwise_and operation:  
    1 1 = 1
    1 0 = 0
    0 1 = 0
    0 0 = 0
    
    """
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # imshow takes in the frame title and the frame value return by the above line and display
    cv2.imshow('Frame Title', result)

    # Wait for 10 millisecond and if in that x millisecond you press 'q' it will break out of the loop.
    if cv2.waitKey(10) == ord('q'):
        break

# This release the camera resources so another program can use it.
cap.release()

cv2.destroyAllWindows()
