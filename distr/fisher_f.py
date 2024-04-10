import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f


def save_to(directory: str, extension: str):
    def y(x, dfn, dfd):
        y = f.pdf(x, dfn, dfd)
        y[y > 2.1] = np.nan
        return y

    # Degrees of freedom for the distribution
    d1_d2 = [(1, 1), (2, 1), (5, 2), (10, 1), (100, 100)]
    # Possible values for the distribution
    x = np.linspace(0, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of the degrees of freedom
    for m, n in d1_d2:
        ax.plot(x, y(x, m, n), label=f'm = {m}, n = {n}')

    # Adding title and labels
    ax.set_title('F-distribution')
    ax.set_xlabel('F statistic')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/fisher_f.{extension}")
    plt.close()
