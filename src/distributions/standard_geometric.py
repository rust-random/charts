import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom


def save_to(directory: str, extension: str):
    # Possible outcomes for a Geometric distributed variable
    outcomes = np.arange(1, 11)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PMF for the standard Geometric distribution
    ax.bar(outcomes, geom.pmf(outcomes, 0.5), label=f'p = 0.5')

    # Adding title and labels
    ax.set_title('Standard Geometric distribution')
    ax.set_xlabel('Number of trials until first success')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax * 1.05)

    plt.savefig(f"{directory}/standard_geometric.{extension}")
    plt.close()
