import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class UpdateRotate:
    def __init__(self, ax):
        ax.set_aspect("equal")
        x_list, y_list = np.meshgrid(np.arange(-10, 10), np.arange(-10, 10))
        self.coords = np.stack((x_list.flatten(), y_list.flatten()), axis = 0)

    def __call__(self, i):
        ax.set_aspect("equal")

        theta = ((i / 150) * 2 * math.pi)
        rotation_matrix = np.array([[np.cos(theta), np.sin(theta)],[-np.sin(theta), np.cos(theta)]])
        transformed_points = rotation_matrix @ self.coords

        ax.clear()
        ax.set_ylim(-5, 5)
        ax.set_xlim(-5, 5)
        ax.scatter((2, 2, -2, -2), (2, -2, 2, -2), color = "red", s = 10)
        self.scatter = ax.scatter(transformed_points[0], transformed_points[1], color = "blue", marker = "+")

        return self.scatter,


fig, ax = plt.subplots()


ud = UpdateRotate(ax)
#interval is how long, and frames is number of frames
anim = FuncAnimation(fig, ud, frames=450, interval=40, blit=True)
anim.save("test.mp4", dpi=250, bitrate=8192)

# plt.show()
