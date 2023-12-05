import numpy as np
import math as mt

class Integrator:
    def __init__(self, xMin, xMax, N):
        self.xMin = xMin
        self.xMax = xMax
        self.N = N

    def integrate(self):
        xtheta = (self.xMax - self.xMin)/self.N
        arr = np.arange(self.N)
        arr = arr*xtheta
        arr = arr + self.xMin
        print(arr)
        for i in range(self.N):
            arr[i] = arr[i]*arr[i]*mt.exp(-arr[i])*mt.sin(arr[i])
        arr = arr*xtheta 
        return np.sum(arr)
    def show(self):
        print(self.integrate())

integration = Integrator(1, 3, 200000)
integration.show()
        
        

