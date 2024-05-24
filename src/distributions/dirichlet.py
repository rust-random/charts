import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from math import gamma
import ternary


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

    def draw_pdf_contours(ax, alphas, nlevels=200, subdiv=8):
        refiner = tri.UniformTriRefiner(triangle)
        trimesh = refiner.refine_triangulation(subdiv=subdiv)
        pvals = [Dirichlet(alphas).pdf(xy2bc(xy)) for xy in zip(trimesh.x, trimesh.y)]

        contour = ax.tricontourf(trimesh, pvals, nlevels, cmap='plasma')
        ternary.plt.colorbar(contour, ax=ax, orientation='vertical', fraction=0.05, pad=0.05)

        ax.axis('equal')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        tax = ternary.TernaryAxesSubplot(ax=ax, scale=1.0)

        tax.boundary(linewidth=1.0)

        tax.ticks(axis='lbr', linewidth=1, multiple=0.2, tick_formats="%.1f", offset=0.02)

        fontsize = 13
        tax.set_title(f"α = {alphas}", fontsize=fontsize, pad=20)
        tax.right_axis_label("$x_3$", fontsize=fontsize, offset=0.15)
        tax.left_axis_label("$x_1$", fontsize=fontsize, offset=0.15)
        tax.bottom_axis_label("$x_2$", fontsize=fontsize)
        tax._redraw_labels()  # Won't do this automatically because of the way we are saving the plot

        tax.clear_matplotlib_ticks()

    inputs = [
        [1.5, 1.5, 1.5],
        [5.0, 5.0, 5.0],
        [1.0, 2.0, 2.0],
        [2.0, 4.0, 8.0]
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    for ax, alphas in zip(axes.flatten(), inputs):
        draw_pdf_contours(ax, alphas)

    # Adding the main title and colorbar
    ternary.plt.suptitle('Dirichlet Distribution', fontsize=16)

    ternary.plt.savefig(f"{directory}/dirichlet.{extension}", bbox_inches='tight', pad_inches=0.5)
    plt.close()
