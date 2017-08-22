#!/usr/local/bin/python3
# -*-coding:utf-8 -*-
"""
# ==================================================
# Name          : log_thing
# Action        : self class
# Explanation   : DateTime  - 時間日期的標記
#               : Timer     - 時間計算
#               : LogThing  - error, info 記錄
#               : DocOut    - 相關內容輸出
# ==================================================
"""

from pytz import timezone
import datetime
import time
import subprocess


class DateTime(object):
    """
* ==================================================
* Self Class    : DateTime
* Extends       : object
* Explanation   : 時間日期的標記
* ==================================================
    """

    def __init__(self):
        # self.result = subprocess.run(["date"], stdout=subprocess.PIPE)
        # result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
        # subprocess.run(["date"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        # result.stdout
        result = subprocess.run(["date"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        return

    @staticmethod
    def printTime():
        print("\n~ Log # Time # " + datetime.datetime.now().strftime("%Y-%m-%d (%a) # %H:%M:%S,%f"))
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

    def __init__(self, classObject: object):
        """
        Info: get class
        :param classObject: object, test.
        """
        super().__init__()
        self._classObject = classObject
        try:
            self._name = self._classObject.__name__
        except Exception as e:
            self._name = classObject
            print(e)

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
    def _operation_time(deltaTime: float):
        """
        Info: operate time to hour, min, s, ms.
        :param deltaTime: float, delta time.
        :return: listTime = [hour, min, s, ms]: [int, int, int, int], time list.
        """
        listTime = [0, 0, 0, 0]

        if deltaTime > 3600000:
            listTime[0] = int(deltaTime / 3600000)
            deltaTime = deltaTime % 3600000

        if deltaTime > 60000:
            listTime[1] = int(deltaTime / 60000)
            deltaTime = deltaTime % 60000

        if deltaTime > 1000:
            listTime[2] = int(deltaTime / 1000)
            listTime[3] = deltaTime % 1000

        return listTime

    def timerStart(self):
        """
        Info: timer start
        """
        self._time_start = time.time() * 1000

        print("\n# # %s ==> Start" % self._name)

    def timerNow(self, remind: str = ""):
        """
        Info: timer now
        :param remind: str, need to remind
        """
        self._time_end = time.time() * 1000
        deltaTime = float(self._time_end - self._time_start)
        timeList = self._operation_time(deltaTime)

        print("\n~ # %s 已過時間：%d h, %d min, %d s, %d ms" % (
            remind, timeList[0], timeList[1], timeList[2], timeList[3]))

    def timerEnd(self):
        """
        Info: timer end
        """
        self._time_end = time.time() * 1000
        deltaTime = float(self._time_end - self._time_start)
        timeList = self._operation_time(deltaTime)

        print("\n# # %s ==> End, total time: %d h, %d min, %d s, %d ms" % (
            self._name, timeList[0], timeList[1], timeList[2], timeList[3]))

    def __enter__(self):
        """

        :return: self
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


class DocOut(object):
    """
* ==================================================
* Self Class    : DocOut
* Extends       : object
* Explanation   : 相關內容輸出
* ==================================================
    """

    def __init__(self, file: str, doc: str):
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
