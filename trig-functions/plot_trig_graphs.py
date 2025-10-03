import numpy as np
import matplotlib.pyplot as plt

def plot_trig_graphs():
    x = np.linspace(-2*np.pi, 2*np.pi, 400)
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.plot(x, np.tan(x), label='tan(x)')
    plt.ylim(-2, 2)
    plt.legend()
    plt.title('Trigonometric Functions')
    plt.xlabel('x (radians)')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_trig_graphs()
