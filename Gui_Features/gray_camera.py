import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
i=1
if not cap.isOpened():
    print("cannot open camera")
    exit()
while True:
    #frame capture
    ret, frame = cap.read()
    
    if not ret:
        print("can't receive frame (stream end?). Exiting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    
    if cv.waitKey(1) == ord('q'):
        break
    
    if cv.waitKey(1) == ord('s'):
        cv.imwrite('Gui_Features/gray'+str(i)+'.jpg',gray)
        cv.imshow('gray'+str(i),gray)
        i+=1
        
        
cap.release()
cv.destroyAllWindows()