import numpy as np
import matplotlib.pyplot as plt


def save_to(directory: str, extension: str):
    # Possible values for the distribution
    x = np.linspace(-7, 7, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    inputs = [(0, 1), (0, 0.5), (0, 2), (-2, 1)]

    # Plotting the PDF for the Cauchy distribution
    for x0, gamma in inputs:
        ax.plot(x, 1 / (np.pi * gamma * (1 + ((x - x0) / gamma)**2)), label=f'x₀ = {x0}, γ = {gamma}')

    # Adding title and labels
    ax.set_title('Cauchy distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)

    plt.savefig(f"{directory}/cauchy.{extension}")
    plt.close()
