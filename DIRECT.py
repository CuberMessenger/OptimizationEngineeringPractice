import numpy as np

from TargetDomain import F, StartPoint, x1Range, x2Range

class DIRECT2D:
    def __init__(self, function, inputRanges) -> None:
        '''
        Actually this implementation is DISQUARE(Divide Squares)
        function = RxR -> R
        inputRange = [
            [x1Min, x1Max],
            [x2Min, x2Max]
        ]
        '''
        self.RestoreX1 = lambda x1: (inputRanges[0][1] - inputRanges[0][0]) * x1 + inputRanges[0][0]
        self.RestoreX2 = lambda x2: (inputRanges[1][1] - inputRanges[1][0]) * x2 + inputRanges[1][0]

        self.NormalizedFunction = lambda x1, x2: function(self.RestoreX1(x1), self.RestoreX2(x2))

        # Squares = [
        #   [(centerX1, centerX2, criteria), ...] # Squares with sidelength = 1 / 1
        #   [(centerX1, centerX2, criteria), ...] # Squares with sidelength = 1 / 2
        #   ...
        # ]
        self.Squares = [
            [
                (0.5, 0.5, self.NormalizedFunction(0.5, 0.5))
            ]
        ]

        self.Minimum = self.Squares[0][0][-1]
        self.Answers = [self.Squares[0][0]]

    def AddSquare(self, i, centerX1, centerX2):
        if i + 1 >= len(self.Squares):
            self.Squares.append([])
        
        self.Squares[i].append(
            (centerX1, centerX2, self.NormalizedFunction(centerX1, centerX2))
        )

        self.Minimum = min(self.Minimum, self.Squares[i][-1][-1])
        self.Answers.append([
            self.RestoreX1(self.Squares[i][-1][0]),
            self.RestoreX2(self.Squares[i][-1][1]),
            self.Squares[i][-1][-1]
        ])

    def DIRECT(self, maxIteration):
        iteration = 0
        while iteration < maxIteration:
            # Get potential optimal squares from self.Squares
            potentialOptimalSquares = []
            for i, squares in enumerate(self.Squares):
                potentialOptimalSquare = (None, None, 0x7FFFFFFF)
                for square in squares:
                    if square[-1] < potentialOptimalSquare[-1]:
                        potentialOptimalSquare = square
                if potentialOptimalSquare[0] is not None:
                    potentialOptimalSquares.append((i,) + potentialOptimalSquare[:2])
                    self.Squares[i].remove(potentialOptimalSquare)

            if len(potentialOptimalSquares) == 0:
                return

            # Generate and evaluate new squares 
            for i, centerX1, centerX2 in potentialOptimalSquares:
                quarterSideLength = 0.25 / (i + 1)
                self.AddSquare(i + 1, centerX1 - quarterSideLength, centerX2 + quarterSideLength)
                self.AddSquare(i + 1, centerX1 + quarterSideLength, centerX2 + quarterSideLength)
                self.AddSquare(i + 1, centerX1 - quarterSideLength, centerX2 - quarterSideLength)
                self.AddSquare(i + 1, centerX1 + quarterSideLength, centerX2 - quarterSideLength)

            iteration += 1
            # print(iteration)

def Solve(maxIteration):
    solver = DIRECT2D(F, [(-2, 8), (-2, 8)])
    solver.DIRECT(maxIteration)
    return np.array(solver.Answers)