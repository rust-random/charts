import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto


def save_to(directory: str, extension: str):
    inputs = [(1, 1), (1, 2), (1, 3), (2, 1)]
    # Possible values for the distribution
    x = np.linspace(0, 3, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of alpha
    for scale, shape in inputs:
        ax.plot(x, pareto.pdf(x, shape, scale=scale), label=f'α = {shape}, x$_{{m}}$ = {scale}')

    # Adding title and labels
    ax.set_title('Pareto distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax * 1.05)

    plt.savefig(f"{directory}/pareto.{extension}")
    plt.close()
