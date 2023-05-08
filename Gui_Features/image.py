## [imports]
import cv2 as cv
import sys
import os
## [imports]
## [imread]
#path='C:/Users/lcman/OneDrive - 한양대학교/바탕 화면/개발/Python OpenCV/opencv_python_practice/Gui Features'
#imgname='cats-in-love.jpg'
#full=path+'/'+imgname
img = cv.imread("Gui_Features/cats-in-love.jpg")

#img = cv.imread("./cats-in-love.jpg")
## [imread]
## [empty]
if img is None:
    sys.exit("Could not read the image.")
## [empty]
## [imshow]
cv.imshow("Display window", img)
k = cv.waitKey(0)
## [imshow]
## [imsave]
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
## [imsave]