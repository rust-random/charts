import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def save_to(directory: str, extension: str):
    inputs = [(0, 1), (0, 0.5), (0, 2), (-2, 1)]
    # Possible values for the distribution
    x = np.linspace(-5, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of mu and sigma
    for mu, sigma in inputs:
        ax.plot(x, norm.pdf(x, loc=mu, scale=sigma), label=f'μ = {mu}, σ = {sigma}')

    # Adding title and labels
    ax.set_title('Normal distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/normal.{extension}")
    plt.close()
