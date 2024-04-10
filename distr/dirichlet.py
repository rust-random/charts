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
        # Flatten the grid to pass to the distribution
        XY = np.vstack((X.flatten(), Y.flatten()))

        # Calculate remaining coordinate for the 3-simplex (3D Dirichlet is defined on a triangle in 2D)
        Z = 1 - X - Y
        # Filter out points outside the triangle
        valid = (Z >= 0)
        # Prepare the probability density function (PDF) array
        PDF = np.zeros(X.shape).flatten()

        # Calculate PDF only for valid points
        if np.any(valid):
            # The 3rd coordinate for the Dirichlet distribution
            Z_valid = Z.flatten()[valid]
            # Stack the coordinates for the distribution input
            XYZ_valid = np.vstack((XY[:, valid], Z_valid))
            # Calculate the Dirichlet PDF
            PDF[valid] = dirichlet.pdf(XYZ_valid.T, alpha)

        # Reshape PDF back into the 2D shape of the grid
        PDF = PDF.reshape(X.shape)

        # Create a contour plot on the provided axis
        contour = ax.contourf(X, Y, PDF, levels=15, cmap='Blues')
        # Add a colorbar
        plt.colorbar(contour, ax=ax, pad=0.05, aspect=10)
        # Set limits and labels
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel(r'$x_1$', fontsize=12)
        ax.set_ylabel(r'$x_2$', fontsize=12)
        # Set title for the subplot
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
