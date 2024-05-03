import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


def save_to(directory: str, extension: str):
    def y(x, min_value, mode, max_value, shape):
        a = 1 + shape * (mode - min_value) / (max_value - min_value)
        b = 1 + shape * (max_value - mode) / (max_value - min_value)
        return beta.pdf(x, a, b, loc=min_value, scale=max_value - min_value)

    inputs = [(-1, 0, 1, 4), (-1, 0, 1, 1), (-1, 0, 1, 8), (-1, 0.5, 1, 4)]
    # Adjusting the range of x values to be more meaningful for the PERT distribution
    x = np.linspace(-1.5, 1.5, 1000)  # max_value in inputs is 2, hence 3 is a reasonable upper bound

    # Creating the figure and the axis
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plotting the PDF for each value of min_value, mode, max_value, and shape
    for min_value, mode, max_value, shape in inputs:
        ax.plot(x, y(x, min_value, mode, max_value, shape),
                label=f'min = {min_value}, mode = {mode}, max = {max_value}, shape = {shape}')

    # Adding title and labels
    ax.set_title('PERT Distribution')
    ax.set_xlabel('x')
    ax.set_ylabel('Probability density')

    # Adding a legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.6, box.height])
    ax.legend(loc='upper left', bbox_to_anchor=(1, 0.6))
    ax.grid()
    ax.margins(x=0, y=0)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax * 1.05)

    plt.savefig(f"{directory}/pert.{extension}")
    plt.close()
