import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


def save_to(directory: str, extension: str):
    # Degrees of freedom for the distribution
    df_values = [1, 2, 5, np.inf]
    # Possible values for the distribution
    x = np.linspace(-5, 5, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of the degrees of freedom
    for df in df_values:
        ax.plot(x, t.pdf(x, df), label=f'nu = {df}')

    # Adding title and labels
    ax.set_title('T-distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/student_t.{extension}")
    plt.close()
