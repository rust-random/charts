import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norminvgauss


def save_to(directory: str, extension: str):
    inputs = [(1, 0), (3, 0), (0.1, 0), (1, -0.99), (1, 0.99)]
    # Possible values for the distribution
    x = np.linspace(-5, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots(figsize=(8, 5))

    # Plotting the PDF for the Normal Inverse Gaussian distribution
    for alpha, beta in inputs:
        ax.plot(x, norminvgauss.pdf(x, alpha, beta, 0, 1), label=f'α = {alpha}, β = {beta}')

    # Adding title and labels
    ax.set_title('Normal Inverse Gaussian distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)

    plt.savefig(f"{directory}/normal_inverse_gaussian.{extension}")
    plt.close()
