import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# b = np.matrix([[1, 2], [3, 4]])
# b_asarray = np.asarray(b)

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# plt.show()


# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()

# x = np.linspace(0, 2, 100)  # Sample data.

# # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, x, label='linear')  # Plot some data on the axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the axes.
# ax.set_ylabel('y label')  # Add a y-label to the axes.
# ax.set_title("Simple Plot")  # Add a title to the axes.
# ax.legend()  # Add a legend.
# plt.show()

# x = np.linspace(0, 2, 100)  # Sample data.

# plt.figure(figsize=(5, 2.7), layout='constrained')
# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})
# plt.show()

# fig, ax = plt.subplots(figsize=(5, 2.7))
# x = np.arange(len(data1))
# ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
# l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
# l.set_linestyle(':')
# plt.show()

# fig, ax = plt.subplots(figsize=(5, 2.7))
# ax.plot(data1, 'o', label='data1')
# ax.plot(data2, 'd', label='data2')
# ax.plot(data3, 'v', label='data3')
# ax.plot(data4, 's', label='data4')
# ax.legend()
# plt.show()

# mu, sigma = 115, 15
# x = mu + sigma * np.random.randn(10000)
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# # the histogram of the data
# n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

# ax.set_xlabel('Length [cm]')
# ax.set_ylabel('Probability')
# ax.set_title('Aardvark lengths\n (not really)')
# ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
# ax.axis([55, 175, 0, 0.03])
# ax.grid(True)
# plt.show(

fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
xdata = np.arange(len(data1))  # make an ordinal for this
data = 10**data1
axs[0].plot(xdata, data)

axs[1].set_yscale('log')
axs[1].plot(xdata, data)
plt.show()
