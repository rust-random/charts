import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


def save_to(directory: str, extension: str):
    def y(x, min_value, mode, max_value, shape):
        a = 1 + shape * (mode - min_value) / (max_value - min_value)
        b = 1 + shape * (max_value - mode) / (max_value - min_value)
        return beta.pdf(x, a, b, loc=min_value, scale=max_value - min_value)
    inputs = [(0, 1, 2, 4)]
    # Possible values for the distribution
    x = np.linspace(0, 100, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of a, b, and c
    for min, mode, max, shape in inputs:
        ax.plot(x, y(x, min, max, mode, shape), label=f'a = {min}, b = {mode}, c = {max}, shape = {shape}')

    # Adding title and labels
    ax.set_title('Pert distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/pert.{extension}")
    plt.close()
