import numpy as np
import cv2 as cv
import datetime
import os

cap = cv.VideoCapture(0)
i = 1
selected_images = []
try:
    os.mkdir('gray')
finally:
    print("gray directory founded")
    


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
        if len(selected_images) < 4:
            print("Select at least four images by pressing 's' before 'q'.")
        else:
            selected_images = [cv.resize(img, (0, 0), fx=0.5, fy=0.5) for img in selected_images]
            montage = np.hstack(selected_images)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            result_filename = 'gray/result_' + timestamp + '.jpg'
            cv.imshow('Montage', montage)
            cv.imwrite(result_filename, montage)
            cv.waitKey(0)
            break

    if key == ord('w'):
        if len(selected_images) < 4:
            print("Select at least four images by pressing 's' before 'w'.")
        else:
            montage = np.vstack(selected_images)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            result_filename = 'gray/result_' + timestamp + '.jpg'
            cv.imshow('Montage', montage)
            cv.imwrite(result_filename, montage)
            cv.waitKey(0)
            break

    if key == ord('s'):
        cv.imwrite('gray/' + str(i) + '.jpg', gray)
        cv.imshow('gray' + str(i), gray)
        i += 1
        selected_images.append(gray)
        if len(selected_images) >= 4:
            print("Press 'q' to display the selected images horizontally or 'w' to display them vertically.")

cap.release()
cv.destroyAllWindows()
