import numpy as np

from TargetDomain import F, StartPoint

class DIRECT2D:
    def __init__(self, function, inputRanges) -> None:
        '''
        function = RxR -> R
        inputRange = [
            [x1Min, x1Max],
            [x2Min, x2Max]
        ]
        '''
        self.Function = function
        self.NormalizedFunction = lambda x1, x2: function(
            (inputRanges[0][1] - inputRanges[0][0]) * x1 + inputRanges[0][0],
            (inputRanges[1][1] - inputRanges[1][0]) * x2 + inputRanges[1][0]
        )

        # Squares = [[x1, x2, criteria, sideLength], ...]
        self.Squares = [[0.5, 0.5, self.NormalizedFunction(0.5, 0.5), 1]]

    def DIRECT(self, maxIteration):
        minF = 0x7FFFFFFF

        i = 0
        while i < maxIteration:
            # Get potential optimal squares from self.Squares
            potentialOptimalSquares = []
            for square in self.Squares:
                pass
            pass

            # Generate and evaluate new squares 
            pass


            i += 1

        return minF
    

def GetCenter(p0, p1):
    return (p0 + p1) / 2

def DIRECT_(p0, p1):
    '''
    p0------
    |       |
    |       |
     ------p1
    '''

    pass