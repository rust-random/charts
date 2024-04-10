import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


def save_to(directory: str, extension: str):
    inputs = [(10, 0.2), (10, 0.6)]
    # Possible outcomes for a Binomial distributed variable
    outcomes = np.arange(0, 11)
    width = 0.5

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PMF for each value of n and p
    for i, (n, p) in enumerate(inputs):
        ax.bar(outcomes + i * width - width / 2, binom.pmf(outcomes, n, p), width=width, label=f'n = {n}, p = {p}')

    # Adding title and labels
    ax.set_title('Binomial distribution')
    ax.set_xlabel('k (number of successes)')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/binomial.{extension}")
    plt.close()
