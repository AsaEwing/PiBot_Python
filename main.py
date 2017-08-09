"""
# ==================================================
# Name: main
# 負責 PiBot 的整體運作
#
# ==================================================
"""

from module_for_all import log_thing
import sys
import os


timer = log_thing.Timer("PiBot_Python.main")
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
