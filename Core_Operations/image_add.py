import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread('kitten.jpg')
img2 = cv.imread('Gui_Features/cats-in-love.jpg')
img2 = cv.resize(img2, dsize=(img1.shape[1], img1.shape[0]), interpolation=cv.INTER_LINEAR)
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

dst = cv.addWeighted(img1,0.5,img2,0.5,0)
dst2= cv.add(img1,img2)
cv.imshow('dst',dst)
cv.imshow('dst2',dst2)
cv.waitKey(0)
cv.destroyAllWindows()
