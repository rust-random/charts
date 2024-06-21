import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom


def save_to(directory: str, extension: str):
    # Possible values of p for the distribution
    p_values = [0.2, 0.5, 0.8]
    # Possible outcomes for a Geometric distributed variable
    outcomes = np.arange(0, 10)

    # Creating the figure and the axis
    fig, ax = plt.subplots()
    width = 0.2

    # Plotting the PMF for each value of p
    for i, p in enumerate(p_values):
        # Specify loc=-1 correct for the difference in the definition of the geometric distribution in scipy
        # and the definition in the rand crate
        ax.bar(outcomes + i * width - width, geom.pmf(outcomes, p, loc=-1), width=width, label=f'p = {p}')

    # Adding title and labels
    ax.set_title('Geometric distribution')
    ax.set_xlabel('Number of failures before first success')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax * 1.05)

    plt.savefig(f"{directory}/geometric.{extension}")
    plt.close()
