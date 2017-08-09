"""
# ==================================================
# Name: log_thing
#
# 1. 時間計算: Timer
# 2. 日期時間標記: DateTime
# ==================================================
"""

import datetime
import time
import subprocess


class Timer(object):
    def __init__(self, name):
        self.Time_AllStart = time.time() * 1000
        self.Time_End = 0
        self.name = name

        print("\n# # %s ==> Start" % self.name)
        return

    @staticmethod
    def operation_time(deltaTime):
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

    def now(self, remind=""):
        self.Time_End = time.time() * 1000
        deltaTime = float(self.Time_End - self.Time_AllStart)
        timeList = self.operation_time(deltaTime)

        if timeList[0] > 0:
            print('\n~ # %s 已過時間：%d h, %d min, %d s, %d ms' % (
                remind, timeList[0], timeList[1], timeList[2], timeList[3]))

        elif timeList[1] > 0:
            print('\n~ # %s 已過時間：%d h, %d min, %d s, %d ms' % (
                remind, timeList[0], timeList[1], timeList[2], timeList[3]))
        elif timeList[2] > 0:
            print('\n~ # %s 已過時間：%d h, %d min, %d s, %d ms' % (
                remind, timeList[0], timeList[1], timeList[2], timeList[3]))
        else:
            print('\n~ # %s 已過時間：%d h, %d min, %d s, %d ms' % (
                remind, timeList[0], timeList[1], timeList[2], timeList[3]))

        return

    def end(self):
        self.Time_End = time.time() * 1000
        deltaTime = float(self.Time_End - self.Time_AllStart)
        timeList = self.operation_time(deltaTime)

        print('\n# # %s ==> End, total time: %d h, %d min, %d s, %d ms' % (
            self.name, timeList[0], timeList[1], timeList[2], timeList[3]))

        return


class DateTime(object):
    def __init__(self):
        # self.result = subprocess.run(['date'], stdout=subprocess.PIPE)
        # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
        # subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        # result.stdout
        result = subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return

    def printTime(self):
        print("\n~ Log # Time # "+datetime.datetime.now().strftime('%Y-%m-%d (%a) # %H:%M:%S,%f'))
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


class ErrorLog(object):
    def __init__(self):
        return
