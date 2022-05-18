import numpy as np

from TargetDomain import F, StartPoint

def Solve(step, epsilon, maxIteration):
    # [(x1, x2, z)]
    x1, x2 = StartPoint
    z = F(x1, x2)

    answer = [(x1, x2, z)]

    iteration = 0
    while True:
        iteration += 1
        # dF/dx1 = 2sin(x1) + sin(x1 - x2)
        dFdx1 = 2 * np.sin(x1) + np.sin(x1 - x2)
        # dF/dx2 = sin(x2) - sin(x1 - x2)
        dFdx2 = np.sin(x2) - np.sin(x1 - x2)

        nextX1 = x1 - step * dFdx1
        nextX2 = x2 - step * dFdx2
        nextZ = F(nextX1, nextX2)

        answer.append((nextX1, nextX2, nextZ))
        if iteration >= maxIteration or abs(nextZ - z) < epsilon:
            break
        x1, x2, z = nextX1, nextX2, nextZ

    return np.array(answer)
