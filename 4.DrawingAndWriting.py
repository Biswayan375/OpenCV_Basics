import cv2 as cv
import numpy as np

width, height = 1000, 500

# Creating an empty image
imgArr = np.zeros((height, width, 3), dtype = 'uint8')
cv.imshow('BlackImage', imgArr)

# Drawing a red box using array slicing
# imgArr[0:100, 0:300] = [0, 0, 200] # The format is BGR instead of RGB
# cv.imshow('RedBoxImage', imgArr)

# Drawing a rectangle in the image
cv.rectangle(imgArr, (100, 100), (400, 400), (150, 150, 150), thickness = 2)  # cv2.rectangle(image_matrix, point1, point2, color, thickness = <an integer value to specify the thickness. However, if you want to totally fill the rectangle then a value of -1 should be given or cv.FILLED should be used>)
# cv.imshow('Rectangle', imgArr)

# Drawing a circle in the image
# cv.circle(imgArr, (200, 200), 50, (0, 150, 0), thickness = 2)
cv.circle(imgArr, (200, 200), 100, (0, 150, 0), thickness = -1)
# cv.imshow('Circle', imgArr)

# Drawing a line in the image
cv.line(imgArr, (200, 200), (400, 400), (255, 255, 255))
# cv.imshow('Drawing', imgArr)

# Writing a text into the image
cv.putText(imgArr, "Hello World", (imgArr.shape[1] // 2, imgArr.shape[0] // 2), 2, 2, (255, 25, 255), thickness = 3)
cv.imshow('Drawing and Writing', imgArr)

cv.waitKey(0)