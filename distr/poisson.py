import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def save_to(directory: str, extension: str):
    # Possible values of lambda for the distribution
    lambda_values = [0.5, 1, 2, 4, 10]
    # Possible outcomes for a Poisson distributed variable
    outcomes = np.arange(0, 15)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PMF for each value of lambda
    for i, lmbda in enumerate(lambda_values):
        ax.plot(outcomes, poisson.pmf(outcomes, lmbda), 'o-', label=f'λ = {lmbda}')

    # Adding title and labels
    ax.set_title('Poisson distribution')
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Probability')
    ax.set_xticks(outcomes)  # set the ticks to be the outcome values

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/poisson.{extension}")
    plt.close()
