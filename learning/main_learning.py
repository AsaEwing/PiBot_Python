"""
# ==================================================
# Name: main_learning
# 負責 神經網路 的整體運作
# ==================================================
"""

from module_for_all import log_thing
from learning.module import tf_class
import sys
import os

timer = log_thing.Timer("PiBot_Python.learning.main_learning")
nowTime = log_thing.DateTime()


def mainEnd():

    """ End """

    timer.end()
    nowTime.printTime()
    return


def mainStart():

    """ Start """

    nowTime.printTime()
    timer.now("Start")

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
