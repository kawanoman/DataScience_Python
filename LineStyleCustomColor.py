import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.DataFrame({'x_values': range(1,11), 'y_values': np.random.randn(10) })

# Draw plot
plt.plot( 'x_values', 'y_values', data=df, color='black', linewidth=12)
#pltraw line chart by modifiying transparency of the line
plt.plot( 'x_values', 'y_values', data=df, color='skyblue', alpha=1)

# Show plot
plt.show()

plt.plot( [1,1.1,1,1.1,1], linestyle='-' , linewidth=4)
plt.text(1.5, 1.3, "linestyle = '-' ", horizontalalignment='left', size='medium', color='C0', weight='semibold')
plt.plot( [2,2.1,2,2.1,2], linestyle='--' , linewidth=4 )
plt.text(1.5, 2.3, "linestyle = '--' ", horizontalalignment='left', size='medium', color='C1', weight='semibold')
plt.plot( [3,3.1,3,3.1,3], linestyle='-.' , linewidth=4 )
plt.text(1.5, 3.3, "linestyle = '-.' ", horizontalalignment='left', size='medium', color='C2', weight='semibold')
plt.plot( [4,4.1,4,4.1,4], linestyle=':' , linewidth=4 )
plt.text(1.5, 4.3, "linestyle = ':' ", horizontalalignment='left', size='medium', color='C3', weight='semibold')
plt.axis('off')
plt.show()
