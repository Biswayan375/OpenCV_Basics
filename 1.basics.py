import cv2 as cv

"""
	cv2.imread() method is used to read images. The first argument is the path to
	the image and the second argument is an integer that specifies the mode in which
	the image is to be read. 0 for grayscale, 1 for colored and -1 for colored with
	alpha channel.
"""

image = cv.imread('ImagesAndVideos/image.jpg') # reading images
print(image) # If the image is not found then value at image variable will be None
cv.imshow('Arya Image', image) # first argument is the name of the window and second one is the image matrix

# cv.waitKey(5000) # Waits for 5000ms before automatically closing the image window

pressed_key = cv.waitKey(0) # Waits for an infinite amount of time before automatically closing the image window

if pressed_key == ord('s'):
	# Checking if 's' key is pressed
	# If pressed then we want to save a copy of the image before destroying the image window
	cv.imwrite("ImagesAndVideos/image_copy.jpg", image) # Creates an image out of given image matrix and saves it in given folder as given name
	print("Successfully saved a copy!")
	cv.destroyAllWindows() # Destroys all windows
elif pressed_key == 27:
	# Checking if 'esc' is pressed
	# If pressed, then we just want to destroy the image window without saving a copy
	cv.destroyAllWindows()