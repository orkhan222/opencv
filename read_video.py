import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('red_panda_snow.mp4')

fourcc = cv2.VideoWriter()

while True:
    ret, frame = cap.read()
    # gary_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.flip(frame, 1)

    # cv2.imshow('gary_scale', gary_scale)
    cv2.imshow('frame', frame2)
    cv2.imshow('flipping', frame)

    # cv2.waitKey(1)
    # key = cv2.waitKey(1)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()