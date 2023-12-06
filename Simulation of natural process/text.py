import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y = np.sin(x)


   
plt.ylabel('$a(t),c(t)$',fontsize=20)
plt.xlabel('$t$', fontsize=20)
plt.plot(x, y)
plt.legend(loc=2,prop={'size':20})
plt.show()
