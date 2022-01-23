import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
	width, height = frame.shape[1], frame.shape[0]
	aspect_ratio = width / height

	new_width = int(width * scale)
	new_height = int(new_width / aspect_ratio)

	dimension = (new_width, new_height)
	return cv.resize(frame, dimension)


# A video is a collection of frames
capture = cv.VideoCapture('ImagesAndVideos/video.mp4')

while True:
	"""
		The capture.read() method actually returns two return values.
		One boolean, isTrue and the other one is the frame. isTrue is
		false when the video is over, or there is no more frame to read.
	"""

	isTrue, frame = capture.read()
	if not isTrue: break
	frame = rescaleFrame(frame, 0.31)
	cv.imshow('Video', frame)

	if cv.waitKey(20) & 0xFF == ord('d'): break # I don't know what the hell this does till now. But without this, the code breaks.

capture.release()
cv.destroyAllWindows()