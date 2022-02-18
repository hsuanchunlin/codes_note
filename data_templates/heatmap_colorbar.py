import matplotlib.pyplot as plt
import numpy as np

# some arbitrary data to plot
x = numpy.linspace(0, 2*numpy.pi, 30)
y = numpy.linspace(0, 2*numpy.pi, 20)
[X, Y] = numpy.meshgrid(x, y)
Z = numpy.sin(X)*numpy.cos(Y)

fig = plt.figure()
plt.ion()
plt.set_cmap('bwr') # a good start: blue to white to red colormap

# a plot ranging from -1 to 1, hence the value 0 (the average) is colorcoded in white
ax = fig.add_subplot(1, 2, 1)
plt.pcolor(X, Y, Z)
plt.colorbar()

# a plot ranging from -0.2 to 0.8 hence 0.3 (the average) is colorcoded in white
ax = fig.add_subplot(1, 2, 2)

# define your scale, with white at zero
vmin = -0.2 
vmax = 0.8
norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)

plt.pcolor(X, Y, Z, vmin=vmin, vmax=vmax, norm=norm)   
plt.colorbar()

#Create loops
def plot_heatmap(data, howmany=2, color_key='bwr'):
    fig = plot.figure()
    fig.ion()
    fig.set_cmap(color_key)
    for i in range(howmany):
        ax = fig.add_subplot(1, howmany, i+1)
        ax.matshow(data[i])
        plt.colorbar(cax)
