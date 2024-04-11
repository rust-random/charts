import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norminvgauss


def save_to(directory: str, extension: str):
    inputs = [(1, 0, 0, 1), (3, 0, 0, 1), (1, 0.9, 0, 1), (1, 0, -1, 1), (1, 0, 0, 3)]
    # Possible values for the distribution
    x = np.linspace(-5, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots(figsize=(8, 5))

    # Plotting the PDF for the Normal Inverse Gaussian distribution
    for alpha, beta, mu, delta in inputs:
        ax.plot(x, norminvgauss.pdf(x, alpha, beta, mu, delta), label=f'α = {alpha}, β = {beta}, μ = {mu}, δ = {delta}')

    # Adding title and labels
    ax.set_title('Normal Inverse Gaussian distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/normal_inverse_gaussian.{extension}")
    plt.close()
