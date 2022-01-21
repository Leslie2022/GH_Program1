import numpy as np
import os

A=np.array([[5,7,9],[3,2,8],[7,6,1]])
b=np.array([65,38,41])

x=np.linalg.solve(A,b)
print(x)