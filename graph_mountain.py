import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm # imports color map tools

f = lambda x, y: np.sin(x) * np.cos(y)
x = np.linspace(-3,3,50)
y = np.linspace(-3,3,50)
X, Y = np.meshgrid(x, y)
F = f(X, Y)

fig = plt.figure(figsize = [12,8])
ax = fig.gca(projection = '3d') # set up he axis as a 3D plot
ax.plot_surface(X, Y, F)
plt.show()