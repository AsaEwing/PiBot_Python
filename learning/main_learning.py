#!/usr/local/bin/python3
# -*-coding:utf-8 -*-
"""
# ==================================================
# Name              : main_learning
# Action            : main for learning
# Explanation       : 負責『神經網路』的整體運作
# Self Class used   : Timer, tf_class
# ==================================================
"""



import sys
import os
from functools import wraps
print("###")
print(sys.path)
print("###")
print(__file__)
print("###")

from module_for_all import log_thing
from learning.module import tf_class

class main_learning(log_thing.Timer):
    """
* ==================================================
* Self Class    : main_learning
* Extends       : log_thing.Timer
* Explanation   : 負責『神經網路』的整體運作
* ==================================================
    """

    def __init__(self):
        """
        1. need to super, send a class object
        2. use Tensorflow
        3. use Webcam to collect data for train
        """

        super().__init__(self.__class__)

        # self.timer = None
        # self.nowTime = log_thing.DateTime()
        return

    def mainEnd(self):
        """ End """

        # self.timer.end()
        # self.nowTime.printTime()
        # return
        self.timerEnd()
        return

    def mainStart(self):
        """ Start """
        # self.timer = log_thing.Timer("PiBot_Python.learning.main_learning")
        # self.nowTime.printTime()
        # self.timer.now("Start")

        self.timerStart()
        self.mainEnd()
        # return
        return


if __name__ == "__main__":
    main = main_learning()
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
