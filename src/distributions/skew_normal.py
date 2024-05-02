import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm


def save_to(directory: str, extension: str):
    inputs = [-5, -2, 0, 2, 5]
    # Possible values for the distribution
    x = np.linspace(-5, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of alpha
    for alpha in inputs:
        ax.plot(x, skewnorm.pdf(x, alpha), label=f'α = {alpha}')

    # Adding title and labels
    ax.set_title('Skew Normal distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)

    plt.savefig(f"{directory}/skew_normal.{extension}")
    plt.close()
