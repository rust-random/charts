import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from math import gamma
from matplotlib import ticker


# Code source: https://blog.bogatron.net/blog/2014/02/02/visualizing-dirichlet-distributions/
class Dirichlet(object):
    def __init__(self, alpha):
        self._alpha = np.array(alpha)
        self._coef = gamma(np.sum(self._alpha)) / np.multiply.reduce([gamma(a) for a in self._alpha])

    def pdf(self, x):
        """Returns pdf value for `x`."""
        return self._coef * np.multiply.reduce([xx ** (aa - 1) for (xx, aa) in zip(x, self._alpha)])


def save_to(directory: str, _: str):
    extension = "png"  # Hardcode png output format. SVG file size for this distribution is ~100x larger.
    corners = np.array([[0, 0], [1, 0], [0.5, np.sqrt(0.75)]])
    AREA = 0.5 * 1 * np.sqrt(0.75)
    triangle = tri.Triangulation(corners[:, 0], corners[:, 1])

    pairs = [corners[np.roll(range(3), -i)[1:]] for i in range(3)]
    tri_area = lambda xy, pair: 0.5 * np.linalg.norm(np.cross(*(pair - xy)))

    def xy2bc(xy, tol=1.e-4):
        coords = np.array([tri_area(xy, p) for p in pairs]) / AREA
        return np.clip(coords, tol, 1.0 - tol)

    def draw_pdf_contours(ax, dist, alphas, nlevels=200, subdiv=8):
        refiner = tri.UniformTriRefiner(triangle)
        trimesh = refiner.refine_triangulation(subdiv=subdiv)
        pvals = [dist.pdf(xy2bc(xy)) for xy in zip(trimesh.x, trimesh.y)]

        contour = ax.tricontourf(trimesh, pvals, nlevels, cmap='plasma')
        ax.axis('equal')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, np.sqrt(0.75))
        ax.axis('on')
        ax.set_title(f"α = {alphas}", fontsize=10)

        return contour

    inputs = [
        [1.5, 1.5, 1.5],
        [5.0, 5.0, 5.0],
        [1.0, 2.0, 2.0],
        [2.0, 4.0, 8.0]
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    contours = []
    for ax, alphas in zip(axes.flatten(), inputs):
        contour = draw_pdf_contours(ax, Dirichlet(alphas), alphas)
        contours.append(contour)

    # Adding the main title and colorbar
    plt.suptitle('Dirichlet Distribution', fontsize=16)
    cbar = fig.colorbar(contours[0], ax=axes.ravel().tolist(), orientation='horizontal', pad=0.75)
    cbar.set_label('Probability Density')
    cbar.ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=5))  # Set number of ticks on colorbar

    plt.subplots_adjust(top=0.90, bottom=0.25)  # Adjust the subplots to fit the title and colorbar
    plt.savefig(f"{directory}/dirichlet.{extension}")
    plt.close()
