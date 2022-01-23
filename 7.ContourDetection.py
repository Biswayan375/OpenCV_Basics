import cv2 as cv
import MyUtils as mu
import numpy as np

"""
    Contours are boundaries of objects, a line or curve that joins
    the continuous points along the boundaries of an object and they
    are not the same as edges.

    cv.findContours(a, b, c) ->
        This method is used in OpenCV to find contours in an image.
    It takes in three parameters, a is the canny edges of the image, b is 
    the mode in which the contour is to be found and c is the contour 
    approximation method. It looks into the edges of the image and returns
    a python list all the coordinates of the contours found in the image
    and the hierarchy of the contours (for say a square inside a rectangle
    that is inside a circle...)

    b: There are several contour finding modes in OpenCV like RETR_LIST 
    that returns a python list of coordinates of all of the contours in 
    the image, RETR_EXTERNAL that returns only the external contours in 
    the image, RETR_TREE that returns the hierarchical contours in the 
    image etc.

    c: There are also several contour approximation methods. CHAIN_APPROX_NONE
    does nothing and returns all the coordinates of the contour. For example,
    if we have a line as a contour, CHAIN_APPROX_NONE will make the function
    return the coordinates of all points on that line. But, CHAIN_APPROX_SIMPLE
    will make the function return only the two end points of that line as
    we can represent a line using only two points.
"""

img = mu.resize_image(cv.imread('./ImagesAndVideos/image1.jpg'), 0.15)

blank_img = np.zeros((img.shape[0], img.shape[1]), dtype = 'uint8')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur_img = cv.GaussianBlur(gray_img, (5, 5), cv.BORDER_DEFAULT)

ret, thresh = cv.threshold(gray_img, 90, 255, cv.THRESH_BINARY)

canny_img = cv.Canny(thresh, 20, 60)

contours, hierarchies = cv.findContours(canny_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found in the image')
cv.drawContours(blank_img, contours, -1, (255, 255, 255))
cv.imshow('Contours', blank_img)

cv.imshow('Gray', gray_img)
cv.imshow('Canny', canny_img)
# cv.imshow('Blurred', blur_img)
cv.imshow('Thresholding', thresh)

cv.waitKey(0)