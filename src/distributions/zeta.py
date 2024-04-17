import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zipf


def save_to(directory: str, extension: str):
    inputs = [3, 2, 1.5, 1.1]  # Different values of s and n
    outcomes = np.arange(1, 11)  # Outcomes from 1 to 10

    # Creating the figure
    fig, ax = plt.subplots()
    width = 0.2  # Bar width

    # Plotting the Zipf Distribution for each value of s
    for i, s in enumerate(inputs):
        ax.bar(outcomes + i * width - width / 2, zipf.pmf(outcomes, s), width=width, label=f's = {s}')

    ax.set_title('Zipf Distribution')
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # Adjusting x-ticks to center
    ax.legend()

    # Save the plot to a file
    plt.savefig(f"{directory}/zeta.{extension}")
    plt.close()
