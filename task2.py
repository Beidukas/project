%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 10, 1000)
k1=4
k2=7
plt.plot(x, np.sin(k1*x))
plt.plot(x, np.sin(k2*x))