import cv2
import numpy as np


template = cv2.imread('template.png', 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

cap = cv2.VideoCapture(0)

while(True):
    
    # Input
    ret, frame = cap.read()
    
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply template Matching
    res = cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where(res >= threshold)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


