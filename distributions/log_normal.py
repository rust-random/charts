import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm


def save_to(directory: str, extension: str):
    inputs = [(0, 1), (0, 0.5), (0, 2), (-0.5, 1), (1, 1)]
    # Possible values for the distribution
    x = np.linspace(0, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of mu and sigma
    for mu, sigma in inputs:
        ax.plot(x, lognorm.pdf(x, s=sigma, scale=np.exp(mu)), label=f'μ = {mu}, σ = {sigma}')

    # Adding title and labels
    ax.set_title('Log-normal distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/log_normal.{extension}")
    plt.close()
