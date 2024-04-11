import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zipf


def save_to(directory: str, extension: str):
    # Possible values of a for the distribution
    a_values = [1.5, 2, 3]
    # Possible outcomes for a Zipf distributed variable
    outcomes = np.arange(1, 11)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PMF for each value of a
    for i, a in enumerate(a_values):
        ax.bar(outcomes + i * 0.2 - 0.1, zipf.pmf(outcomes, a), width=0.2, label=f'a = {a}')

    # Adding title and labels
    ax.set_title('Zipf distribution')
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/zipf.{extension}")
    plt.close()
