#!/usr/local/bin/python3
# -*-coding:utf-8 -*-
"""
# ==================================================
# Name          : log_thing
# Action        : self class
# Explanation   : DateTime  - 時間日期的標記
#               : Timer     - 時間計算
#               : LogThing  - error, info 記錄
# ==================================================
"""

import datetime
import time
import subprocess


class DocOut(object):
    """
* ==================================================
* Self Class    : DocOut
* Extends       : object
* Explanation   : 相關內容輸出
* ==================================================
    """
    def __init__(self, file, doc):
        """

        :param file: str,   use __file__
        :param doc: str,    use __doc__
        """
        self._file = file
        self._doc = doc
        return

    def output(self):
        """

        :return:
        """
        print("\nPython3 Running:")
        print("\n        " + self._file)
        print(self._doc)


class DateTime(object):
    """
* ==================================================
* Self Class    : DateTime
* Extends       : object
* Explanation   : 時間日期的標記
* ==================================================
    """

    def __init__(self):
        # self.result = subprocess.run(['date'], stdout=subprocess.PIPE)
        # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
        # subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        # result.stdout
        result = subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return

    @staticmethod
    def printTime():
        print("\n~ Log # Time # " + datetime.datetime.now().strftime('%Y-%m-%d (%a) # %H:%M:%S,%f'))
        return

    def getYear(self):
        return

    def getMonth(self):
        return

    def getDay(self):
        return

    def getHour(self):
        return

    def getMinute(self):
        return

    def getSecond(self):
        return


class Timer(DateTime):
    """
* ==================================================
* Self Class    : Timer
* Extends       : DateTime
* Explanation   : 時間計算
* ==================================================
    """

    def __init__(self, classObject):
        """

        :param classObject: object, test.
        """
        super().__init__()
        self._classObject = classObject
        self._name = self._classObject.__name__

        self._time_start = 0
        self._time_end = 0
        return

    def __call__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        return

    def __get__(self, instance, owner):
        """

        :param instance:
        :param owner:
        :return:
        """
        return

    @staticmethod
    def _operation_time(deltaTime):
        """

        :param deltaTime:
        :return:
        """
        mHour = 0
        mMin = 0
        mS = 0
        mMs = 0
        if deltaTime > 3600000:
            mHour = int(deltaTime / 3600000)
            deltaTime = deltaTime % 3600000
        if deltaTime > 60000:
            mMin = int(deltaTime / 60000)
            deltaTime = deltaTime % 60000
        if deltaTime > 1000:
            mS = int(deltaTime / 1000)
            mMs = deltaTime % 1000

        return [mHour, mMin, mS, mMs]

    def timerStart(self):
        """

        :return:
        """
        self._time_start = time.time() * 1000

        print("\n# # %s ==> Start" % self._name)
        return

    def timerNow(self, remind=""):
        """

        :param remind:
        :return:
        """
        self._time_end = time.time() * 1000
        deltaTime = float(self._time_end - self._time_start)
        timeList = self._operation_time()

        print('\n~ # %s 已過時間：%d h, %d min, %d s, %d ms' % (
            remind, timeList[0], timeList[1], timeList[2], timeList[3]))
        return

    def timerEnd(self):
        """

        :return:
        """
        self._time_end = time.time() * 1000
        deltaTime = float(self._time_end - self._time_start)
        timeList = self._operation_time(deltaTime)

        print('\n# # %s ==> End, total time: %d h, %d min, %d s, %d ms' % (
            self._name, timeList[0], timeList[1], timeList[2], timeList[3]))

        return

    def __enter__(self):
        """

        :return:
        """
        self.timerStart()
        return self

    def __exit__(self, *args):
        """

        :param args:
        :return:
        """
        self.timerEnd()


class LogThing(object):
    """
* ==================================================
* Self Class    : LogThing
* Extends       : object
* Explanation   : error, info 記錄
* ==================================================
    """

    def __init__(self):
        return
