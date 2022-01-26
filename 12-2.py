import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 1000)
y = -x**3 + x**2
plt.plot(x, y, color='b')
plt.xlabel('Probability')
plt.ylabel('Likelihood')

x_plt = 2/3
y_plt = -x_plt**3 + x_plt**2
new_x = [2/3-0.1, 2/3, 2/3+0.1]
new_y = [-x_plt**3 + x_plt**2 for i in new_x ] 
plt.plot(x_plt, y_plt, '-o', color='r')
plt.plot(new_x, new_y, color='r')
plt.grid()
plt.show()
