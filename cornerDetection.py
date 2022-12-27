import numpy as np
import cv2

img = cv2.imread('media/images/chessboard.png')

# Resize this picture
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# convert to grayscale, this good for the algorithm
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
Using the Shi-Tomasi Corner Detection algorithm

goodFeaturesToTrack() takes in the following arguments:
    - Source image.
    - Number of corners you want to return in int, return the N best number of corner.
    - Minimum quality of our corne between 0,1 , 1 will be a perfect corner.
    - Minimum Euclidean distance between corners, by passing this value you are telling the program to only display the corner if it greater that value. 
      Euclidean distance is the absolute distance between two points on a graph
    
"""
corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)
corners = np.int0(corners)  # convert the corners value into integers

for corner in corners:
    x, y = corner.ravel()  # This does [[1,2],[2,3]] -> [1,2,2,3]
    # Draw the corners
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)


# Uncomment the folowing line to draw lines between your points
# for i in range(len(corners)):
#     for j in range(len(corners)):
#         corner1 = tuple(corners[i][0])
#         corner2 = tuple(corners[j][0])
#         color = tuple(map(lambda x:int(x), np.random.randint(0,255,size=3)))
#         cv2.line(img,corner1,corner2,color,1)


cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
