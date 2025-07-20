# Convert .txt file into .mat file for prediction

import os
from time import time, sleep
import numpy as np
import scipy
from scipy import io

a = np.loadtxt('sc1.txt', dtype = 'object')
a1 = a[100:9100]
print(type(a1[150]))

a1 = np.asarray(a1, dtype = 'float64')

a1 = a1.reshape(1,-1)
scipy.io.savemat('sc1.mat', {'val': a1})