import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom


def save_to(directory: str, extension: str):
    # Possible values of p for the distribution
    p_values = [0.2, 0.5, 0.8]
    # Possible outcomes for a Geometric distributed variable
    outcomes = np.arange(1, 11)

    # Creating the figure and the axis
    fig, ax = plt.subplots()
    width = 0.2

    # Plotting the PMF for each value of p
    for i, p in enumerate(p_values):
        ax.bar(outcomes + i * width - width / 2, geom.pmf(outcomes, p), width=width, label=f'p = {p}')

    # Adding title and labels
    ax.set_title('Geometric distribution')
    ax.set_xlabel('Number of trials until first success')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/geometric.{extension}")
    plt.close()
