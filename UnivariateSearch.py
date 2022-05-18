import numpy as np

from TargetDomain import F, StartPoint

def Bisection(targetFunction, epsilon, xm, radius):
    xa = xm - radius
    xb = xm + radius
    xm = (xa + xb) / 2
    fa = targetFunction(xa)
    fb = targetFunction(xb)
    fm = targetFunction(xm)

    answer = [(xm, fm)]

    while True:
        xl = (xa + xm) / 2
        xr = (xm + xb) / 2
        fl = targetFunction(xl)
        fr = targetFunction(xr)

        minX = 0
        minY = 0x7FFFFFFF
        for x, y in zip([xa, xl, xm, xr, xb], [fa, fl, fm, fr, fb]):
            if y < minY:
                minX = x
                minY = y

        answer.append((minX, minY))

        if abs(xa - xb) < epsilon:
            break

        if minY in [fa, fl]:
            xb = xm
            xm = xl
            fb = fm
            fm = fl
        if minY == fm:
            xa = xl
            xb = xr
            fa = fl
            fb = fr
        if minY in [fr, fb]:
            xa = xm
            xm = xr
            fa = fm
            fm = fr
    return answer

def Solve(cycle, epsilon):
    x1, x2 = StartPoint
    z = F(x1, x2)

    answer = [(x1, x2, z)]

    while cycle > 0:
        cycle -= 1

        functionRespectToX1 = lambda x: F(x, x2)
        x1Answer = Bisection(functionRespectToX1, epsilon, x1, 3)
        answer += [(x1Trace, x2, zTrace) for x1Trace, zTrace in x1Answer]
        x1 = x1Answer[-1][0]

        functionRespectToX2 = lambda x: F(x1, x)
        x2Answer = Bisection(functionRespectToX2, epsilon, x2, 3)
        answer += [(x1, x2Trace, zTrace) for x2Trace, zTrace in x2Answer]
        x2 = x2Answer[-1][0]

    return np.array(answer)
