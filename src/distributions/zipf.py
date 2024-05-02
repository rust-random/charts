import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zipfian


def save_to(directory: str, extension: str):
    inputs = [(2, 10), (1, 10), (0, 10)]  # Different values of s and n
    outcomes = np.arange(1, 12)  # Outcomes from 1 to 10

    # Creating the figure
    fig, ax = plt.subplots()
    width = 0.2  # Bar width

    # Plotting the Zipf Distribution for each value of s
    for i, (s, n) in enumerate(inputs):
        ax.bar(outcomes + i * width - width / 2, zipfian.pmf(outcomes, s, n), width=width, label=f's = {s}, n = {n}')

    ax.set_title('Zipf Distribution')
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # Adjusting x-ticks to center
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)

    # Save the plot to a file
    plt.savefig(f"{directory}/zipf.{extension}")
    plt.close()
