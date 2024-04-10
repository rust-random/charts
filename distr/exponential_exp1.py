import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon


def save_to(directory: str, extension: str):
    # Fixed value for lambda
    lmbda = 1
    # Possible values for the distribution
    x = np.linspace(0, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of lambda
    ax.plot(x, expon.pdf(x, scale=1 / lmbda), label=f'λ = {lmbda}')

    # Adding title and labels
    ax.set_title('Exponential distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/exponential_exp1.{extension}")
    plt.close()
