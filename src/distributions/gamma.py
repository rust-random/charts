import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma


def save_to(directory: str, extension: str):
    inputs = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2)]
    # Possible values for the distribution
    x = np.linspace(0, 7, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()
    colors = ["blue", "red", "green", "blue", "red", "green"]
    alphas = [1.0, 1.0, 1.0, 0.6, 0.6, 0.6]

    # Plotting the PDF for each value of alpha and beta
    for i, (k, theta) in enumerate(inputs):
        ax.plot(x, gamma.pdf(x, k, scale=theta), label=f'k = {k}, θ = {theta}', color=colors[i], alpha=alphas[i])

    # Adding title and labels
    ax.set_title('Gamma distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)

    plt.savefig(f"{directory}/gamma.{extension}")
    plt.close()
