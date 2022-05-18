import numpy as np

from TargetDomain import F, StartPoint, AdditionalStartPoints, x1Range, x2Range

def Solve(epsilon):
    def PointF(p):
        return F(p[0], p[1])
    # For two variables, simplex is a triangle
    xs = np.array([
            np.array(StartPoint),
            np.array(AdditionalStartPoints[0]),
            np.array(AdditionalStartPoints[1])
        ]
    )

    answer = []
    triangles = []

    while True:
        Fs = np.array([PointF(x) for x in xs])
        maxIndex = np.argmax(Fs)
        minIndex = np.argmin(Fs)

        xw = xs[maxIndex]
        xb = xs[minIndex]
        Fw = Fs[maxIndex]
        Fb = Fs[minIndex]

        answer.append((xb[0], xb[1], Fb))
        triangles.append([])
        for x in xs:
            triangles[-1].append((x[0], x[1], PointF(x)))
        triangles[-1].append((xs[0][0], xs[0][1], PointF(xs[0])))

        xSurf = (np.sum(xs, axis = 0) - xw) / (len(xs) - 1)
        xBar = np.mean(xs, axis = 0)

        xp = xw + 2 * (xSurf - xw)
        Fp = PointF(xp)

        contracted = False
        if Fp < Fb:
            xpp = xp + xp - xw
            if PointF(xpp) < Fp:
                xp = xpp
            xw = xp
        else:
            if Fp < Fw:
                xw = xp
            else:
                xp = xw + 4 * (xSurf - xw) / 3
                Fp = PointF(xp)
                if Fp < Fw:
                    xw = xp
                else:
                    for i in range(len(xs)):
                        if i != minIndex:
                            xs[i] = 0.5 * (xs[i] + xb)
                        print("Contracted!")
                        contracted = True

        if not contracted:
            xs[maxIndex] = xw
            # if xw[0] >= x1Range[0] and xw[0] <= x1Range[1] and xw[1] >= x2Range[0] and xw[1] <= x2Range[1]:
            #     xs[maxIndex] = xw
            # else:
            #     for i in range(len(xs)):
            #         if i != minIndex:
            #             xs[i] = 0.5 * (xs[i] + xb)

        answer.append((xb[0], xb[1], Fb))
        triangles.append([])
        for x in xs:
            triangles[-1].append((x[0], x[1], PointF(x)))
        triangles[-1].append((xs[0][0], xs[0][1], PointF(xs[0])))

        delta = 0
        for x in xs:
            delta += np.sqrt(np.sum((x - xBar) ** 2))
        delta /= len(xs)

        if delta < epsilon:
            break
    return np.array(answer), np.array(triangles)


