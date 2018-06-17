import pyautogui as ptg
import math

def move(x=None, y=None):

    screenWidth, screenHeight = ptg.size()
    screenWidthMiddle = screenWidth / 2
    screenHeightMiddle = screenHeight / 2

    print(screenWidthMiddle)
    print(screenHeightMiddle)

    if not x:
        ptg.moveTo(screenWidthMiddle, screenHeightMiddle, 0.7)


import numpy as np

Q =[45,456,47,123,4]
del Q[0]
print (Q)