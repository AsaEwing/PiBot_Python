#!/usr/local/bin/python3
# -*-coding:utf-8 -*-
"""
# ==================================================
# Name              : main_eye
# Action            : main for webcam
# Explanation       : 負責『 Webcam 』的整體運作
# Self Class used   : Timer, camera
# ==================================================
"""

from module_for_all import log_thing
from eye.module.webcam import Camera
import numpy as np
import cv2
import sys
import os


class main_eye(log_thing.Timer):
    """
* ==================================================
* Self Class    : main_eye
* Extends       : log_thing.Timer
* Explanation   : 負責『 Webcam 』的整體運作
* ==================================================
    """

    def __init__(self):
        super().__init__(self.__class__)
        self._eye = Camera(cv2.VideoCapture(0))
        self._eyeHeight = 0
        self._eyeWidth = 0
        return

    def mainEnd(self):

        """ End """

        self._eye.getCapture().release()
        cv2.destroyAllWindows()

        self.timerEnd()
        self.printTime()
        return

    def mainStart(self):

        """ Start """

        self.printTime()
        self.timerStart()

        if self._eye.getCapture().isOpened():
            self._eyeHeight, self._eyeWidth = self._eye.getSize()
            print("\nOriginal Height :", self._eyeHeight)
            print("\nOriginal Width  :", self._eyeWidth)

            self._eye.setSize(height=960, width=544)

            eyeHeight, eyeWidth = self._eye.getSize()
            print("\nNow Height :", eyeHeight)
            print("\nNow Width  :", eyeWidth)

        while self._eye.getCapture().isOpened():
            retval, frame = self._eye.getCapture().read()

            if retval:
                # frame = cv2.flip(frame, 0)
                edges = cv2.Canny(frame, 100, 200)
                sobelx8u = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)

                cv2.imshow("frame", frame)
                # cv2.imshow("frame2", edges)
                # cv2.imshow("frame3", sobelx8u)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break

        self.mainEnd()
        return


if __name__ == "__main__":
    main = main_eye()
    log_thing.DocOut(__file__, __doc__).output()

    try:
        main.mainStart()

    except KeyboardInterrupt:
        print("\nInterrupted\n")
        main.mainEnd()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
