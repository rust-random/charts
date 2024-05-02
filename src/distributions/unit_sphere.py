import numpy as np
import matplotlib.pyplot as plt


def save_to(directory: str, extension: str):
    # Create a sphere
    def plot_sphere(radius=1, num_divisions=50):
        phi = np.linspace(0, np.pi, num_divisions)  # polar angle
        theta = np.linspace(0, 2 * np.pi, num_divisions)  # azimuthal angle

        # Meshgrid
        phi, theta = np.meshgrid(phi, theta)
        x = radius * np.sin(phi) * np.cos(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(phi)

        return x, y, z

    # Plotting parameters
    radius = 1
    num_divisions = 50  # Increase this for a smoother sphere

    x, y, z = plot_sphere(radius, num_divisions)

    # Create a plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, color='b', alpha=0.6, rstride=1, cstride=1)

    # Scaling the axes
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_aspect('auto')
    ax.set_box_aspect([1, 1, 1])

    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Unit Sphere (shell)')

    # Save the figure
    plt.savefig(f"{directory}/unit_sphere.{extension}")
    plt.close()
