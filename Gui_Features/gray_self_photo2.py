import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
i = 1
selected_images = []
display_gray = False  # Flag to indicate grayscale or color display

if not cap.isOpened():
    print("Cannot open camera")
    exit()

def on_switch(value):
    global display_gray
    if value == 0:
        display_gray = False
    else:
        display_gray = True

# Create a named window for the frame
cv.namedWindow('frame')

# Create a trackbar switch
cv.createTrackbar('Display', 'frame', 0, 1, on_switch)

while True:
    # Frame capture
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    if display_gray:
        display_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    else:
        display_frame = frame

    cv.imshow('frame', display_frame)

    key = cv.waitKey(1)

    if key == ord('q'):
        if len(selected_images) < 4:
            print("Select at least four images by pressing 's' before 'q'.")
        else:
            selected_images = [cv.resize(img, (0, 0), fx=0.5, fy=0.5) for img in selected_images]
            montage = np.hstack(selected_images)
            cv.imshow('Montage', montage)
            cv.imwrite('opencv_python_practice/Gui_Features/result.jpg', montage)
            cv.waitKey(0)
            break

    if key == ord('w'):
        if len(selected_images) < 4:
            print("Select at least four images by pressing 's' before 'w'.")
        else:
            montage = np.vstack(selected_images)
            cv.imshow('Montage', montage)
            cv.imwrite('opencv_python_practice/Gui_Features/result.jpg', montage)
            cv.waitKey(0)
            break

    if key == ord('s'):
        cv.imwrite('opencv_python_practice/Gui_Features/gray/' + str(i) + '.jpg', display_frame)
        cv.imshow('gray' + str(i), display_frame)
        i += 1
        selected_images.append(display_frame)
        if len(selected_images) >= 4:
            print("Press 'q' to display the selected images horizontally or 'w' to display them vertically.")

cap.release()
cv.destroyAllWindows()
