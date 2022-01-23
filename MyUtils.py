import cv2 as cv
import numpy as np

def resize_image(frame, scale = 0.3):
    """Resizes given frame by specified scaling factor maintaining its original aspect ratio"""
    org_width, org_height = frame.shape[1], frame.shape[0]
    aspect_ratio = org_width / org_height

    new_width = int(org_width * scale)
    new_height = int(new_width / aspect_ratio)
    return cv.resize(frame, (new_width, new_height), interpolation = cv.INTER_CUBIC)


def translate_image(frame, x, y):
    """Translates the given frame by x along x-axis and by y along y-axis"""
    trans_mat, dimension = np.float32([[1, 0, x], [0, 1, y]]), (frame.shape[1], frame.shape[0])
    return cv.warpAffine(frame, trans_mat, dimension)


def rotate_image(frame, angle, scale = 1.0, point = None):
    """Rotates the given frame by given angle (in degrees) by the given point. scale is the scaling factor which is to be applied
    to the image when rotating. By default it is 1 which means no scaling is applied"""
    width, height = frame.shape[1], frame.shape[0]

    if point is None:
        # If no center point is given, then the image will be rotated by the center point of the image frame.
        point = (width // 2, height // 2)
    
    rotation_matrix = cv.getRotationMatrix2D(point, angle, scale)
    return cv.warpAffine(frame, rotation_matrix, (width, height))


def scale_image(frame, sx = 1.0, sy = 1.0):
    """Scales the given frame by sx along x-axis and by sy along y-axis"""
    scale_mat, dimension = np.float32([[sx, 0, 1], [0, sy, 1]]), (frame.shape[1], frame.shape[0])
    return cv.warpAffine(frame, scale_mat, dimension)


def flip_image(frame, flag = "horizontally"):
    """Flips the given image. flag can be either 'horizontally' or 'vertically' or 'both'"""
    if flag not in ['horizontally', 'vertically', 'both']: return None
    if flag == 'vertically': flip_code = 0
    elif flag == 'horizontally': flip_code = 1
    else: flip_code = -1

    return cv.flip(frame, flip_code)