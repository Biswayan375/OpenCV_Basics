import cv2 as cv

def resize_image(frame, scale = 0.3):
    """Resizes given frame by specified scaling factor maintaining its original aspect ratio"""
    org_width, org_height = frame.shape[1], frame.shape[0]
    aspect_ratio = org_width / org_height

    new_width = int(org_width * scale)
    new_height = int(new_width / aspect_ratio)
    return cv.resize(frame, (new_width, new_height), interpolation = cv.INTER_CUBIC)


img = cv.imread('./ImagesAndVideos/image1.jpg')
cv.imshow('Original Image', resize_image(img))

# Converting an image to GrayScale
gray = resize_image(cv.cvtColor(img, cv.COLOR_BGR2GRAY))
# cv.imshow('Gray Image', gray)


# Blurring the image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Gaussian Blurred Image', resize_image(blur, 0.2))


# Edge Cascade -> Edge detection using built-in Canny Edge Detector
canny = cv.Canny(img, 10, 80)
cv.imshow('Canny Edges', resize_image(canny))


# Dialating the image -> The edges get thicker when dilating an image from its structural image
dilated = cv.dilate(resize_image(canny), (3, 3), iterations = 1)
cv.imshow('Dilated Image', dilated)


# Eroding the image -> We get back the structual images from the dilated image using eroding
eroded = cv.erode(dilated, (3, 3), iterations = 1)
cv.imshow('Eroded Image', eroded)


# Cropping the image
cropped = resize_image(img)[100:400, 200:500]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)