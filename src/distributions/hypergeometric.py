import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom


def save_to(directory: str, extension: str):
    inputs = [(50, 12, 10), (50, 35, 10)]
    # Possible outcomes for a Hypergeometric distributed variable
    outcomes = np.arange(0, 10)
    width = 0.5

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PMF for each value of N, K, and n
    for i, (N, K, n) in enumerate(inputs):
        ax.bar(outcomes + i * width - width / 2, hypergeom.pmf(outcomes, N, K, n), width=width, label=f'N = {N}, K = {K}, n = {n}')

    # Adding title and labels
    ax.set_title('Hypergeometric distribution')
    ax.set_xlabel('k (number of successes)')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)

    plt.savefig(f"{directory}/hypergeometric.{extension}")
    plt.close()
