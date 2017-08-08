import numpy as np
import cv2


class camera(object):
    def __init__(self, videoCapture):
        self._cap = videoCapture
        self._width = self._cap.get(3)
        self._height = self._cap.get(4)
        return

    def getSize(self):
        return self._height, self._width

    def setSize(self, height=640, width=480):
        self._cap.set(3, height)
        self._cap.set(4, width)
        return

    def getCapture(self):
        return self._cap

    def openShow(self):
        return
