import numpy as np

StartPoint = -2.6, 1.8
AdditionalStartPoints = [(-2.5, 1.6), (-2.3, 1.8)]
# AdditionalStartPoints = [(2.3, 0), (0, -2)]
x1Range = -5, 5
x2Range = -5, 5

def F(x1, x2):
    return -2 * np.cos(x1) - np.cos(x2) - np.cos(x1 - x2)

def GetGrid():
    x1 = np.arange(x1Range[0], x1Range[1], 0.1)
    x2 = np.arange(x2Range[0], x2Range[1], 0.1)
    xGrid, yGrid = np.meshgrid(x1,x2)
    zGrid = F(xGrid, yGrid)
    return x1, x2, xGrid, yGrid, zGrid
