import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2


def save_to(directory: str, extension: str):
    def y(x, df):
        y = chi2.pdf(x, df)
        y[y > 1.0] = np.nan
        return y
    # Degrees of freedom for the distribution
    df_values = [1, 2, 3, 5, 9]
    # Possible values for the distribution
    x = np.linspace(0, 10, 1000)

    # Creating the figure and the axis
    fig, ax = plt.subplots()

    # Plotting the PDF for each value of the degrees of freedom
    for df in df_values:
        ax.plot(x, y(x, df), label=f'k = {df}')

    # Adding title and labels
    ax.set_title('Chi-squared distribution')
    ax.set_xlabel('Chi-squared statistic')
    ax.set_ylabel('Probability density')

    # Adding a legend
    ax.legend()

    plt.savefig(f"{directory}/chi_squared.{extension}")
    plt.close()
