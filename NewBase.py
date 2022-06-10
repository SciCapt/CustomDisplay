from newFunctions import *
import pygetwindow as wn
from os import system
import numpy as np
import time

# Set Window to Particular Size and Position
system("title " + 'Game')
time.sleep(.1) # small time delay to allow title to update
GameWindow = wn.getWindowsWithTitle('Game')[0]
GameWindow.resizeTo(790, 810)
GameWindow.moveTo(40, 0)

# Base Array Variables
pixels = xWidth*yWidth
printableArray = blackBlock*xWidth
numericalArray = np.zeros((yWidth,xWidth))

# Dynamic Section
FPS = 20 ## According to tests in ArrayFunctions, multiply wanted FPS by 20/15
FPS = FPS * 26/15
for frames in range(100):

    # Array Updater Function
    numericalArray = Board(numericalArray)

    # Graphical Builder
    for j in range(yWidth):
        for i in range(xWidth):
            try:
                if numericalArray[j,i] == 1:
                    printableArray = printableArray + whiteBlock
                elif numericalArray[j,i] == 0:
                    printableArray = printableArray + blackBlock
                elif numericalArray[j,i] == 2:
                    printableArray = printableArray + barH
                elif numericalArray[j,i] == 3:
                    printableArray = printableArray + barV
            except:
                printableArray = printableArray + blackBlock

    # Print result, reset graphical display, limit refresh rate
    print(printableArray)
    printableArray = blackBlock*xWidth
    time.sleep(1/FPS)
