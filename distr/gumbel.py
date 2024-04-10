import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gumbel_r


def save_to(directory: str, extension: str):
    inputs = [(0, 0.5), (0, 1), (0, 2), (-2, 1)]
    # Possible values for the distribution
    x = np.linspace(-5, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of mu and beta
    for mu, beta in inputs:
        ax.plot(x, gumbel_r.pdf(x, loc=mu, scale=beta), label=f'μ = {mu}, β = {beta}')

    # Adding title and labels
    ax.set_title('Gumbel distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/gumbel.{extension}")
    plt.close()
