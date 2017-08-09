"""
# ==================================================
# Name: main_eye
# 負責 WebCam 的整體運作
# ==================================================
"""

from module_for_all import log_thing
from eye.module.webcam import camera
import numpy as np
import cv2
import sys
import os

timer = log_thing.Timer("PiBot_Python.eye.main_eye")
nowTime = log_thing.DateTime()

eye = camera(cv2.VideoCapture(0))


def mainEnd():

    """ End """

    eye.getCapture().release()
    cv2.destroyAllWindows()

    timer.end()
    nowTime.printTime()
    return


def mainStart():

    """ Start """

    nowTime.printTime()
    timer.now("Start")

    if eye.getCapture().isOpened():
        eyeHeight, eyeWidth = eye.getSize()
        print("\nOriginal Height :", eyeHeight)
        print("Original Width  :", eyeWidth)

        eye.setSize(height=960, width=544)

        eyeHeight, eyeWidth = eye.getSize()
        print("\nNow Height :", eyeHeight)
        print("Now Width  :", eyeWidth)

    while eye.getCapture().isOpened():
        ret, frame = eye.getCapture().read()

        if ret == True:
            # frame = cv2.flip(frame, 0)
            edges = cv2.Canny(frame, 100, 200)
            sobelx8u = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)

            cv2.imshow('frame', frame)
            # cv2.imshow('frame2', edges)
            # cv2.imshow('frame3', sobelx8u)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    mainEnd()
    return


if __name__ == '__main__':
    try:
        mainStart()
    except KeyboardInterrupt:
        print('\nInterrupted\n')
        mainEnd()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
