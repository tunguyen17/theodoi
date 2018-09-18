import cv2
import numpy as np



cap = cv2.VideoCapture(0)

while(True):
    
    # Input
    ret, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    # define the range of blue color in HSV
    lower_blue = np.array([10, 50, 110])
    upper_blue = np.array([30, 80, 180])
    
    
    # Threshold the HSV imange to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    # cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


