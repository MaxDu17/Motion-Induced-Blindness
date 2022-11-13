import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class UpdateRotate:
    def __init__(self, ax):
        ax.set_aspect("equal")
        x_list, y_list = np.meshgrid(np.arange(-6, 7, 2), np.arange(-6, 7, 2))
        self.coords = np.stack((x_list.flatten(), y_list.flatten()), axis = 0)

    def __call__(self, i):
        ax.set_aspect("equal")

        theta = ((i / 150) * 2 * math.pi)
        rotation_matrix = np.array([[np.cos(theta), np.sin(theta)],[-np.sin(theta), np.cos(theta)]])
        transformed_points = rotation_matrix @ self.coords

        ax.clear()
        ax.set_ylim(-10, 10)
        ax.set_xlim(-10, 10)
        ax.set_axis_off()
        # ax.set_facecolor("gray")

        yTick = np.linspace(-10, 10, 50)
        ax.barh(yTick, width = 20, left = -10, height=(yTick[1] - yTick[0]), color=['black', 'gray'])

        stimulus_x = list()
        stimulus_y = list()
        for j in range(20):
            theta = (j / 20) * 2 * math.pi
            stimulus_x.append(4 * math.cos(theta))
            stimulus_y.append(4 * math.sin(theta))


        self.scatter = ax.scatter(transformed_points[0], transformed_points[1], color = "cyan", marker = "+", s = 80)
        # ax.scatter((4, 4, -4, -4), (4, -4, 4, -4), color = "yellow", s = 6)

        ax.scatter(stimulus_x, stimulus_y, color = "yellow", s = 5)
        if (i // 3) % 2 == 0:
            ax.scatter((0,), (0,), color = "green", marker = "+", s = 80)
        else:
            ax.scatter((0,), (0,), color = "red", marker = "+", s = 80)

        return self.scatter,


fig, ax = plt.subplots()


ud = UpdateRotate(ax)
#interval is how long between frames, and frames is number of frames
anim = FuncAnimation(fig, ud, frames=450, interval=20, blit=True)
anim.save("test.mp4", dpi=250, bitrate=8192)

# plt.show()
