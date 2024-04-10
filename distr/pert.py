import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


def save_to(directory: str, extension: str):
    inputs = [(1, 1, 0), (2, 2, 0), (4, 4, 0), (2, 3, 0), (3, 2, 0)]
    # Possible values for the distribution
    x = np.linspace(0, 1, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of a, b, and c
    for a, b, c in inputs:
        ax.plot(x, beta.pdf(x, a, b, loc=c), label=f'a = {a}, b = {b}, c = {c}')

    # Adding title and labels
    ax.set_title('Pert distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/pert.{extension}")
    plt.close()
