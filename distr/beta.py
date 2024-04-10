import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


def save_to(directory: str, extension: str):
    # Defining the Beta distribution PDF
    def y(a, b, x):
        y = beta.pdf(x, a, b)
        y[y > 4] = np.nan
        return y

    inputs = [(0.5, 0.5), (5, 1), (1, 3), (2, 2), (2, 5)]
    # Possible values for the distribution
    x = np.linspace(0, 1, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of alpha and beta
    for a, b in inputs:
        ax.plot(x, y(a, b, x), label=f'α = {a}, β = {b}')

    # Adding title and labels
    ax.set_title('Beta distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/beta.{extension}")
    plt.close()
