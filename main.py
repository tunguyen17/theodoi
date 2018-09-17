import cv2
import numpy as np

# mouse callback function
def draw_circle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, ' - ', y)
        cv2.circle(frame, (x, y), 100, (255, 0, 0), -1)

cv2.namedWindow('frame')

# Capturing video
cap = cv2.VideoCapture(0)

# list of circle
circle_centers = [(50, 110), (200, 150)]

cv2.setMouseCallback('frame', draw_circle)

# loop
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    


    if len(circle_centers) == 0:
        pass
    else:
        for cen in circle_centers:
            cv2.circle(frame, cen, 50, (255, 0, 200), -1)

    # display the frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
