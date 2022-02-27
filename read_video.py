import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gary_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    cv2.imshow('gary_scale', gary_scale)
    cv2.imshow('frame', frame)

    # cv2.waitKey(1)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()