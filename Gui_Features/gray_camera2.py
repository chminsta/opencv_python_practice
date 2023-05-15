import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
i = 1

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Frame capture
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)

    key = cv.waitKey(1)

    if key == ord('q'):
        break

    if key == ord('s'):
        cv.imwrite('opencv_python_practice/Gui_Features/gray/' + str(i) + '.jpg', gray)
        cv.imshow('gray' + str(i), gray)
        i += 1

cap.release()
cv.destroyAllWindows()
