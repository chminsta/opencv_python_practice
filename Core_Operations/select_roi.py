# selectROI로 관심영역 지정 및 표시, 저장 (roi_select_img.py)

import cv2 as cv
import numpy as np

img = cv.imread('Gui_Features\\cats-in-love.jpg')

x,y,w,h	= cv.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
    cv.moveWindow('cropped', 0, 0) # 새창을 화면 좌측 상단에 이동
    cv.imwrite('./cropped2.jpg', roi)   # ROI 영역만 파일로 저장

cv.waitKey(0)
cv.destroyAllWindows()