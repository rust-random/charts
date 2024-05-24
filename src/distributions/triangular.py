import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import triang


def save_to(directory: str, extension: str):
    # Defining the Triangular distribution PDF
    def y(a, b, c, x):
        return triang.pdf(x, c=(c - a) / (b - a), loc=a, scale=b - a)

    inputs = [(0, 1, 0.5), (0, 1, 0.25), (0, 1, 0.75), (-1, 1, 0)]
    # Possible values for the distribution
    x = np.linspace(-1, 1, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of a, b, and c
    for a, b, c in inputs:
        ax.plot(x, y(a, b, c, x), label=f'a = {a}, b = {b}, c = {c}')

    # Adding title and labels
    ax.set_title('Triangular distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax * 1.05)

    plt.savefig(f"{directory}/triangular.{extension}")
    plt.close()
