import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('kitten.jpg')
img2 = cv.resize(img1, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
assert img1 is not None, "file could not be read, check with os.path.exists()"
replicate = cv.copyMakeBorder(img2,100,100,100,100,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img2,100,100,100,100,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img2,100,100,100,100,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img2,100,100,100,100,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img2,100,100,100,100,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img2,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()