import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    
    # draw on the frame (center x, center y), radious, (b, g, r), -1)
    frame = cv2.ellipse(frame, (350, 180), (30, 30), 310, 0, 275, (255, 0, 0), 20)

    frame = cv2.ellipse(frame, (250, 180), (30, 30), 10, 0, 275, (0, 255, 0), 20) 

    frame = cv2.ellipse(frame, (310, 110), (30, 30), 135, 0, 275, (0, 0, 255), 20) 
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(frame,'OpenCV',(210, 270), font, 1.5,(255,255,255),2,cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

