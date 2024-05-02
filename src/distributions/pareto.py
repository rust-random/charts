import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto


def save_to(directory: str, extension: str):
    inputs = [1, 2, 3]
    # Possible values for the distribution
    x = np.linspace(0, 3, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of alpha
    for alpha in inputs:
        ax.plot(x, pareto.pdf(x, alpha), label=f'α = {alpha}')

    # Adding title and labels
    ax.set_title('Pareto distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/pareto.{extension}")
    plt.close()
