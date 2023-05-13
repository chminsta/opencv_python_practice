import numpy as np
import cv2 as cv
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

'''
['EVENT_FLAG_ALTKEY', 
'EVENT_FLAG_CTRLKEY', 
'EVENT_FLAG_LBUTTON', 
'EVENT_FLAG_MBUTTON', 
'EVENT_FLAG_RBUTTON', 
'EVENT_FLAG_SHIFTKEY',
'EVENT_LBUTTONDBLCLK',
'EVENT_LBUTTONDOWN',
'EVENT_LBUTTONUP', 
'EVENT_MBUTTONDBLCLK', 
'EVENT_MBUTTONDOWN', 
'EVENT_MBUTTONUP', 
'EVENT_MOUSEHWHEEL', 
'EVENT_MOUSEMOVE',
'EVENT_MOUSEWHEEL',
'EVENT_RBUTTONDBLCLK', 
'EVENT_RBUTTONDOWN', 
'EVENT_RBUTTONUP']
'''

