import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli


# Bernoulli distribution
def save_to(directory: str, extension: str):
    # Defining the Bernoulli distribution PMF
    def y(p):
        return np.array([1 - p, p])

    # Possible values of p for the distribution
    p_values = [0.1, 0.5, 0.9]
    # Possible outcomes for a Bernoulli distributed variable
    outcomes = np.array([0, 1])

    # Creating the figure and the axis
    fig, ax = plt.subplots()
    # Width of each bar
    width = 0.2

    # Plotting the PMF for each value of p
    for i, p in enumerate(p_values):
        ax.bar(outcomes - width / 2 + i * width - 0.1, y(p), width=width, label=f'p = {p}')

    # Adding title and labels
    ax.set_title('Bernoulli distribution')
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, 1)

    plt.savefig(f"{directory}/bernoulli.{extension}")
    plt.close()
