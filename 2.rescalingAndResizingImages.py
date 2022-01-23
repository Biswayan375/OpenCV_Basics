import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
	"""
		I have used a pretty simple logic to resize the image frame maintaining
		the original aspect ratio of the image.

		First get the original aspect ratio which is original width divided by
		original height. Then scale the width with desired scaling factor. Now,
		you have your scaled width. If you want to maintain the aspect ratio
		then you have to make sure that after resizing also, the aspect ratio
		remains the same, that is new_width / new_height = original_aspect_ratio.
		From this formula, you can derive the new_height pretty simply, that is,
		new_width / original_aspect_ratio.
	"""

	# frame.shape[1] is the width of the frame
	# frame.shape[0] is the height of the frame
	width, height = frame.shape[1], frame.shape[0]

	aspect_ratio = (width / height)

	new_width = int(width * scale)
	new_height = int(new_width / aspect_ratio)

	dimension = (new_width, new_height)
	return cv.resize(frame, dimension)

image = cv.imread('ImagesAndVideos/image.jpg')
image_resized = rescaleFrame(image, 0.25)
cv.imshow('original image', image)
cv.imshow('resized image', image_resized)

cv.waitKey(0)