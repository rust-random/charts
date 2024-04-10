import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def save_to(directory: str, extension: str):
    # Possible values for the distribution
    x = np.linspace(-5, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for the standard normal distribution
    ax.plot(x, norm.pdf(x), label=f'μ = 0, σ = 1')

    # Adding title and labels
    ax.set_title('Standard normal distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/standard_normal.{extension}")
    plt.close()
