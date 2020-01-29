import cv2, numpy


def make_background(size, color):
    bg = numpy.zeros([size[1]*64, size[0]*64, 3])
    bg += color
    return bg.astype(numpy.uint8)
