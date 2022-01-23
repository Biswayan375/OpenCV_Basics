import MyUtils as mu
import cv2 as cv

img = cv.imread('./ImagesAndVideos/image.jpg')
img = mu.resize_image(img)
cv.imshow('Original Image', img)


# Translating the image -> the function translate_image() is defined in MyUtils. The origin (0, 0) is in the top-left as usual.
translated1 = mu.translate_image(img, 50, 50)
translated2 = mu.translate_image(img, -100, 50)
cv.imshow('Translated Image1', translated1)
cv.imshow('Translated Image2', translated2)


# Rotating the image -> the function rotate_image() is defined in MyUtils.
rotated1 = mu.rotate_image(img, 90)
rotated2 = mu.rotate_image(img, 45, scale = 1.5)
cv.imshow('Rotated Image1', rotated1)
cv.imshow('Rotated Image2', rotated2)


# Scaling the image -> the function is defined in MyUtils
scaled = mu.scale_image(img, 1.5)
cv.imshow('Scaled Image', scaled)


# Flipping the image
flipped1 = mu.flip_image(img, 'horizontally')
flipped2 = mu.flip_image(img, 'vertically')
cv.imshow('Flipped Image1', flipped1)
cv.imshow('Flipped Image2', flipped2)



cv.waitKey(0)