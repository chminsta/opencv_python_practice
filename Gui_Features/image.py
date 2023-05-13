## [imports]
import cv2 as cv
import sys
import os
## [imports]
## [imread]
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
    cv.imwrite("Gui_Features/Cats.jpg", img)
