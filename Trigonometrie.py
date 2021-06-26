import matplotlib.pyplot as plt
import numpy as np


#This is a funktion for calculting a product of expo and cos funktion.

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.annotate('local max', xy=(1, 0.4), xytext=(1.5, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
plt.title('Easy as 1, 2, 3') # subplot 211 title
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.title('Easy as 1, 2, 3') # subplot 211 title
plt.axis([0, 10, 0, 2])
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.text(7, 1, r'$\mu=100,\ \sigma=15$')

plt.show()
