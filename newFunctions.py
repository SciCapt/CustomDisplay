import math

# Pixel Printer Values
blackBlock  = '  ' # 0
whiteBlock  = '██' # 1
barH        = '||' # 2
barV        = '--' # 3

# Base Size for Printed Array
xWidth = 47
yWidth = 47

def border(array):
    for j in range(array.shape[0]):
        for i in range(array.shape[1]):
            if j == 0 or j == yWidth-1 or i == 0 or i == xWidth-1:
                array[j,i] = 1
    return array
    ## 100 frames in 5.066s

def fancyBorder(array):
    for j in range(array.shape[0]):
        for i in range(array.shape[1]):
            if j == 0 or j == yWidth-1:
                array[j,i] = 3
            elif i == 0 or i == xWidth-1:
                array[j,i] = 2
    return array
    ## 100 frames in 5.095s

def mathBorder(array):
    for j in range(array.shape[0]):
        for i in range(array.shape[1]):
            if j == yWidth-1:
                array[j,i] = 3
            elif i == 0:
                array[j,i] = 2
    return array
    ## untested

def mathGraph(array):
    # Equation
    def f(x):
        y = 10*math.sin(x/4) + array.shape[0]/2
        return y

    # Draw points
    for i in range(array.shape[1]):
        x = i
        Y = f(x)
        realY = int(array.shape[0]-Y)
        if realY < 0:   # Checks of bounds for y
            continue
        if realY > array.shape[0]-1:
            continue
        array[realY, x] = 1

    # Draw border
    array = mathBorder(array)

    return array
    ## 100 frames in 5.071s

def Board(array):
    for j in range(array.shape[0]):
        for i in range(array.shape[1]):
            if (j%array.shape[0])%2 == 1:
                if (i%array.shape[1])%2 == 1:
                    array[j,i] = 1
                else:
                    array[j,i] = 0
    return array
    ## 100 frames in 5.102s
