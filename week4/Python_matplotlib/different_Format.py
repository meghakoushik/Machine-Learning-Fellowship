import matplotlib.pyplot as plt
import numpy as np


class diff_format:

    def draw_format(self):
        # Sampled time at 200ms intervals
        t = np.arange(0., 5., 0.2)

        # green dashes, blue squares and red triangles
        plt.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^')
        plt.show()


obj = diff_format()
obj.draw_format()
