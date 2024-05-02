import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from math import gamma


# Code source: https://blog.bogatron.net/blog/2014/02/02/visualizing-dirichlet-distributions/
class Dirichlet(object):
    def __init__(self, alpha):
        self._alpha = np.array(alpha)
        self._coef = gamma(np.sum(self._alpha)) / np.multiply.reduce([gamma(a) for a in self._alpha])

    def pdf(self, x):
        """Returns pdf value for `x`."""
        return self._coef * np.multiply.reduce([xx ** (aa - 1) for (xx, aa) in zip(x, self._alpha)])


def save_to(directory: str, _: str):
    extension = "png"  # Hardcode png output format. SVG output for Dirichlet is ~22 MB, while png is ~115KB.
    corners = np.array([[0, 0], [1, 0], [0.5, 0.75 ** 0.5]])
    AREA = 0.5 * 1 * 0.75 ** 0.5
    triangle = tri.Triangulation(corners[:, 0], corners[:, 1])

    # For each corner of the triangle, the pair of other corners
    pairs = [corners[np.roll(range(3), -i)[1:]] for i in range(3)]
    # The area of the triangle formed by point xy and another pair or points
    tri_area = lambda xy, pair: 0.5 * np.linalg.norm(np.cross(*(pair - xy)))

    def xy2bc(xy, tol=1.e-4):
        """Converts 2D Cartesian coordinates to barycentric."""
        coords = np.array([tri_area(xy, p) for p in pairs]) / AREA
        return np.clip(coords, tol, 1.0 - tol)

    def draw_pdf_contours(ax, alphas, nlevels=200, subdiv=8, **kwargs):
        refiner = tri.UniformTriRefiner(triangle)
        trimesh = refiner.refine_triangulation(subdiv=subdiv)
        pvals = [Dirichlet(alphas).pdf(xy2bc(xy)) for xy in zip(trimesh.x, trimesh.y)]

        ax.tricontourf(trimesh, pvals, nlevels, cmap='jet', **kwargs)
        ax.axis('equal')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.75 ** 0.5)
        ax.axis('off')
        ax.text(0.5, -0.1, f"α = {alphas}", ha='center', transform=ax.transAxes)

    inputs = [
        [1.5, 1.5, 1.5],
        [5.0, 5.0, 5.0],
        [1.0, 2.0, 2.0],
        [2.0, 4.0, 8.0]
    ]

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    for ax, alphas in zip(axes.flatten(), inputs):
        draw_pdf_contours(ax, alphas)

    plt.suptitle("Dirichlet Distribution", fontsize=12)

    # Save the figure
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.savefig(f"{directory}/dirichlet.{extension}")
    plt.close()
