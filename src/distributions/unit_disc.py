import numpy as np
import matplotlib.pyplot as plt


def save_to(directory: str, extension: str):
    # Create a circle
    def plot_circle(radius=1, num_divisions=100):
        theta = np.linspace(0, 2 * np.pi, num_divisions)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        return x, y

    # Plotting parameters
    radius = 1
    num_divisions = 100  # Increase this for a smoother circle

    x, y = plot_circle(radius, num_divisions)

    # Create a plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.fill(x, y, color='b', alpha=0.6)

    # Scaling the axes
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')

    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Unit Disc')
    ax.grid()
    ax.margins(x=0, y=0)

    plt.tight_layout()

    # Save the figure
    plt.savefig(f"{directory}/unit_disc.{extension}")
    plt.close()
