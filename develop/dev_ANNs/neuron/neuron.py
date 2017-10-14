#!/usr/local/bin/python3
# -*-coding:utf-8 -*-
"""
# ==================================================
# Name              : neuron
# Action            : module for neuron
# Explanation       : make a module for neuron
# Self Class used   : neuron
# Note              :
# ==================================================
"""

from module_for_all import log_thing
import numpy as np
import random

from module_for_all.log_thing import Basic


class neuron_original(log_thing.Timer):
    """
* ==================================================
* Self Class    : neuron
* Extends       : log_thing.Timer
* Explanation   : 基本單一 neuron 設置
* ==================================================
    """

    def __init__(self, inputX: np.array, outputY: float, weight: np.array, bias: float):
        """
        1. need to super, send a class object
        2. make neuron's basic setting
        """
        super().__init__(self.__class__)

        self.inputX = inputX
        self.outputY = outputY
        self.weight = weight
        self.bias = bias
        return

    def nextInput(self):
        print("### 1")
        return

    def nextWeight(self):
        return

    def nextBias(self):
        return


class neuron(neuron_original):
    """
* ==================================================
* Self Class    : neuron
* Extends       : neuron_original
* Explanation   : 包裝 neuron. 多上了數值檢測, 分配等等
* ==================================================
    """

    def __init__(self, inputArray: list, outputCorrect: float, weight: list = None, bias: float = None, isList=False):
        """
        1. need to super, to make neuron
        2. used to check data
        """

        self.ors_inArray = inputArray
        self.ors_outCorrect = outputCorrect

        self.inArray = None
        self.outCorrect = None

        self.isList = isList

        if weight is None:
            self.weight = random.uniform(0, 1)
            print(self.weight)
        else:
            self.weight = weight

        if bias is None:
            self.bias = random.uniform(0, 1)
            print(self.bias)
        else:
            self.bias = bias

        self.checkAllVar()

        super().__init__(self.inArray, self.outCorrect, self.weight, self.bias)
        return

    def checkAllVar(self):

        self.inArray = self.checkArray("ors_inArray", self.ors_inArray)
        self.outCorrect = self.checkFloat("ors_outCorrect", self.ors_outCorrect)

        return

    def checkArray(self, varName, tmpVar):

        if type(tmpVar) == list:
            tmpVar = np.array(tmpVar)

            if not self.isList:
                print("need to check, is type of \"" + varName + "\" list?")

        elif type(tmpVar) == np.array:
            return tmpVar

        else:
            print("need to check, is type of \"" + varName + "\" list or np.array!")
            return None

        return tmpVar

    def checkFloat(self, varName, tmpVar):

        if type(tmpVar) == int:
            tmpVar = float(tmpVar)

        elif type(tmpVar) == complex:
            print("need to check, type of \"" + varName + "\" need to int or float!")
            return None

        elif type(tmpVar) == float:
            return tmpVar

        else:
            print("need to check, type of \"" + varName + "\" need to int or float!")
            return None

        return tmpVar

    def nextInput(self):
        super().nextInput()
        print("### 2")
        return


"""
x_all = sum(i=1 to n, weight_i * x_i) - bias
y_sigmoid = 1/(1+exp(-x_all)) or 1/(1+5exp(-5*x_all))

diffDelta(p) = y_correct(p) - y_now(p)

weight(p+1) = weight(p) + ΔWeight(p)
ΔWeight(p) = α * y_now(p) * δ(p)

α : 自訂的學習率
δ : 誤差梯度

δ(p) = ∂(y_now(p))/∂(x_all(p)) * diffDelta(p)
     = y_now(p) * (1-y_now(p)) * diffDelta(p)
"""

inX1 = [0, 0, 1, 1, 0, 1, 0, 1]
inX2 = [0, 1, 0, 1, 1, 1, 0, 0]
outCorrect = [0, 0, 0, 1, 0, 1, 0, 0]

tmpNeuron = neuron([inX1[0], inX2[0]], outCorrect[0])
tmpNeuron.nextInput()
tmpNeuron.timerStart()
tmpNeuron.timerNow()
tmpNeuron.timerEnd()
