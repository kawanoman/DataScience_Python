import numpy as np
import matplotlib.pyplot as plt


# Optional: define x for all the sub-plots
x = np.linspace(0,2*np.pi,100)

# (1) Prepare the figure infrastructure 
fig, ax_array = plt.subplots(nrows=2, ncols=2)

# flatten the array of axes, which makes them easier to iterate through and assign
ax_array = ax_array.flatten()

# (2) Plot loop
for i, ax in enumerate(ax_array):
  ax.plot(x , np.sin(x + np.pi/2*i))
  #ax.set_title(f'plot {i}')

# Optional: main title
plt.suptitle('Plots')
