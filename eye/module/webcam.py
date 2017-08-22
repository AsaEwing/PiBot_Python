#!/usr/local/bin/python3
# -*-coding:utf-8 -*-
"""
# ==================================================
# Name          : webcam
# Action        : self class
# Explanation   : Camera   - WebCam 的抽象
# ==================================================
"""

import numpy as np
import cv2


class Camera(object):
    """
* ==================================================
* Self Class    : Camera
* Extends       : object
* Explanation   : WebCam 的抽象
* ==================================================
    """
    def __init__(self, videoCapture):
        """

        :param videoCapture:
        """
        self._cap = videoCapture
        self._width = self._cap.get(3)
        self._height = self._cap.get(4)
        return

    def getSize(self):
        """
        :return: height: int & width: int
        """
        return self._height, self._width

    def setSize(self, height=640, width=480):
        """

        :param height: int
        :param width: int
        :return:
        """
        self._cap.set(3, height)
        self._cap.set(4, width)
        return

    def getCapture(self):
        """

        :return: cap: video capture
        """
        return self._cap

    def openShow(self):
        """

        :return:
        """
        return
