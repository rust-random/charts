import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import dirichlet

def save_to(directory: str, extension: str):
    def plot_dirichlet(alpha, ax):
        """
        Plots a Dirichlet distribution given alpha parameters and axis.
        """
        # Create a 2D meshgrid of points
        resolution = 200  # Resolution of the visualization
        x = np.linspace(0, 1, resolution)
        y = np.linspace(0, 1, resolution)
        X, Y = np.meshgrid(x, y)

        # Calculate remaining coordinate for the 3-simplex (3D Dirichlet is defined on a triangle in 2D)
        Z = 1 - X - Y

        # Filter out points outside the triangle
        valid = Z >= 0

        # Prepare coordinates and the probability density function (PDF) array
        X = X[valid]
        Y = Y[valid]
        Z = Z[valid]
        points = np.vstack((X, Y, Z)).T  # Stack the valid points

        # Calculate the Dirichlet PDF for valid points
        PDF = dirichlet.pdf(points, alpha)

        # Reshape PDF back into a 2D array for contour plotting
        # Initialize full grid PDF to zero (areas outside the triangle remain zero)
        full_PDF = np.zeros((resolution, resolution))
        full_PDF[valid] = PDF  # Place the calculated PDF in the valid grid positions

        # Create a contour plot on the provided axis
        contour = ax.contourf(np.linspace(0, 1, resolution), np.linspace(0, 1, resolution), full_PDF, levels=50, cmap='Blues')
        plt.colorbar(contour, ax=ax, pad=0.05, aspect=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel(r'$x_1$', fontsize=12)
        ax.set_ylabel(r'$x_2$', fontsize=12)
        ax.set_title(r'$\alpha = {}$'.format(alpha), fontsize=14)

    # Define alpha parameters for the Dirichlet distributions to be plotted
    alpha_params = [
        (1.5, 1.5, 1.5),
        (5.0, 5.0, 5.0),
        (1.0, 2.0, 2.0),
        (2.0, 4.0, 8.0)
    ]

    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # Loop through the list of alpha parameters
    for alpha, ax in zip(alpha_params, axes.flatten()):
        plot_dirichlet(alpha, ax)

    plt.savefig(f"{directory}/dirichlet.{extension}")
    plt.close()