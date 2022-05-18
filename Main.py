import plotly
import numpy as np
from sklearn.preprocessing import scale
import GradientDescent
import UnivariateSearch
import Simplex

from TargetDomain import F, GetGrid

'''
Gradient descent
Univariate search
The Nelder and Mead simplex
DIRECT
'''
triangles = None

# answer = GradientDescent.Solve(1e-1, 1e-6, 1e3)
# answer = UnivariateSearch.Solve(10, 1e-4)
answer, triangles = Simplex.Solve(1e-4)

x1, x2, xGrid, yGrid, zGrid = GetGrid()

data = [
    plotly.graph_objects.Surface(
        x = xGrid,
        y = yGrid,
        z = zGrid
    ),
    plotly.graph_objects.Surface(
        x = xGrid,
        y = yGrid,
        z = np.ones_like(zGrid) * (-5),
        surfacecolor = zGrid
    ),
    plotly.graph_objects.Scatter3d(
        x = answer[:, 0],
        y = answer[:, 1],
        z = answer[:, 2],
        mode = "lines",
        line = dict(
            color = "red",
            width = 10
        )
    ),
    plotly.graph_objects.Scatter3d(
        x = answer[:, 0],
        y = answer[:, 1],
        z = np.ones_like(answer[:, 2]) * (-5),
        mode = "lines",
        line = dict(
            color = "black",
            width = 10,
            
        )
    )
]

if triangles is not None:
    for triangle in triangles:
        data.append(
            plotly.graph_objects.Scatter3d(
                x = triangle[:, 0],
                y = triangle[:, 1],
                z = triangle[:, 2],
                mode = "lines",
                line = dict(
                    color = "blue",
                    width = 5
                )
            )
        )

figure = plotly.graph_objects.Figure(
    data = data
)

figure.update_layout(
    width = 2200,
    height = 900
)

figure.show()

# figure.write_image(f"Surface.svg", engine = "orca")
