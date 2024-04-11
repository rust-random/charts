import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min


def save_to(directory: str, extension: str):
    def y(x, alpha):
        y = weibull_min.pdf(x, alpha)
        y[y > 5] = np.nan
        return y
    # Possible values of alpha for the distribution
    alpha_values = [0.1, 0.5, 1, 2, 5, 10]
    # Possible values for the distribution
    x = np.linspace(0, 3, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of alpha
    for alpha in alpha_values:
        ax.plot(x, y(x, alpha), label=f'α = {alpha}')

    # Adding title and labels
    ax.set_title('Weibull distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/weibull.{extension}")
    plt.close()
