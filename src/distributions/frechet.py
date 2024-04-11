import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import invweibull


def save_to(directory: str, extension: str):
    def y(x, shape, loc, scale):
        return invweibull.pdf(x, shape, loc=loc, scale=scale)
    # Inputs for the distribution
    inputs = [(0, 1, 1), (1, 1, 1), (0, 0.5, 1), (0, 2, 1), (0, 1, 0.35), (0, 1, 2)]
    # x values for the distribution
    x = np.linspace(0, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of a
    for loc, scale, shape in inputs:
        ax.plot(x, y(x, shape, loc, scale), label=f'μ = {loc}, σ = {scale}, α = {shape}')

    # Adding title and labels
    ax.set_title('Fréchet distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/frechet.{extension}")
    plt.close()
