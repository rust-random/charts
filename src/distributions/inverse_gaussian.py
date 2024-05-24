import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import invgauss


def save_to(directory: str, extension: str):
    # Possible values for the distribution
    x = np.linspace(0, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    inputs = [(1, 1), (1, 2), (2, 1), (2, 2)]

    # Plotting the PDF for the Inverse Gaussian distribution
    for mu, lambda_ in inputs:
        ax.plot(x, invgauss.pdf(x, mu, scale=lambda_), label=f'μ = {mu}, λ = {lambda_}')

    # Adding title and labels
    ax.set_title('Inverse Gaussian distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax * 1.05)

    plt.savefig(f"{directory}/inverse_gaussian.{extension}")
    plt.close()
