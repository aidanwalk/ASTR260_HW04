import matplotlib.pyplot as plt
import numpy as np

#load data from files
dx = np.loadtxt('dx_potential_data.txt', delimiter=',')
dy = np.loadtxt('dy_potential_data.txt', delimiter=',')

#tame data
dx[dx > 5e10] = None
dx[dx < -5e10] = None
dy[dy > 5e10] = None
dy[dy < -5e10] = None

widths = np.linspace(0, 2, dx.size)
plt.quiver(dx,dy, linewidths=widths)
plt.show()