import matplotlib.pyplot as plt
import numpy as np

def plot_unit_circle():
    theta = np.linspace(0, 2*np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot(x, y)
    plt.gca().set_aspect('equal')
    plt.title('Unit Circle')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_unit_circle()
