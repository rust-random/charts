import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min


def save_to(directory: str, extension: str):
    def y(x, scale, shape):
        y = weibull_min.pdf(x, shape, scale=scale)
        y[y > 5] = np.nan
        return y
    # Possible values of alpha for the distribution
    inputs = [(1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (2, 2)]
    # Possible values for the distribution
    x = np.linspace(0, 3, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of alpha
    for scale, shape in inputs:
        ax.plot(x, y(x, scale, shape), label=f'λ = {scale}, k = {shape}')

    # Adding title and labels
    ax.set_title('Weibull distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax * 1.05)

    plt.savefig(f"{directory}/weibull.{extension}")
    plt.close()
