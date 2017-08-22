#!/usr/local/bin/python3
# -*-coding:utf-8 -*-
"""
# ==================================================
# Name              : main
# Action            : main for all
# Explanation       : 負責『 PiBot 』的整體運作
# Self Class used   : Timer
# Note              : use 'pydoc3 -p 9999' to read doc
# ==================================================
"""

from module_for_all import log_thing
import sys
import os

__author__ = "Asa Ewing"
__version__ = "1.0.0"


class mainPiBot(log_thing.Timer):
    """
* ==================================================
* Self Class    : mainPiBot
* Extends       : log_thing.Timer
* Explanation   : 負責『 PiBot 』的整體運作
* ==================================================
    """

    def __init__(self):
        """
        1. need to super, send a class object
        """

        super().__init__(self.__class__)

        # self.timer = None
        # self.nowTime = log_thing.DateTime()
        return

    def mainEnd(self):
        """ End """

        self.timerEnd()
        self.printTime()
        return

    def mainStart(self):
        """ Start """

        self.printTime()
        self.timerStart()

        self.mainEnd()
        return


if __name__ == "__main__":
    main = mainPiBot()
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
