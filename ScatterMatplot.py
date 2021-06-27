import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dataset:
df = pd.DataFrame({'x_values': range(1, 101), 'y_values': np.random.randn(100) * 15 + range(1, 101)})

# plot
plt.plot('x_values', 'y_values', data=df, marker='o' , color='olive', linewidth=2, linestyle='dashed', label="toto", markerfacecolor='black', markersize=6 )
plt.title('Scatter Plot Basic', fontsize=20)
plt.xlim(0,100,0,150)
plt.xlabel('Time')
plt.ylabel('Work')
plt.legend()
plt.show()
