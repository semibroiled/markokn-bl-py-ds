
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi, 100)
a = plt.figure()
#plt.show(plt.plot(x, np.sin(x)))
plt.plot(x, np.cos(x))
a.show()

#plt.show(x, np.cos(x))
#plt.show()