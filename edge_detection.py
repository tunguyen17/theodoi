import cv2
import numpy as np



cap = cv2.VideoCapture(0)

while(True):
    
    # Input
    ret, frame = cap.read()
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    edge = cv2.Canny(frame, 100, 200)

    # Display the resulting frame
    cv2.imshow('frame', edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


