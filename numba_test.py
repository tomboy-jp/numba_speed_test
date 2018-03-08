from time import time
import numpy as np
from numba import jit

def numpy_only(x, y):

    result = 0
    X = np.random.randn(x)
    Y = np.random.randn(y)
    for x in X:
        for y in Y:
            result += x + y

    return result

@jit
def numba_jit(x, y):

    result = 0
    X = np.random.randn(x)
    Y = np.random.randn(y)
    for x in X:
        for y in Y:
            result += x + y

    return result

print('numpy_only, start!')
start = time()
numpy_only(10000, 10000)
end = time()
print('exe_time: {}[sec]'.format(end - start) + '\n')

print('numba_jit, start!')
start = time()
numba_jit(10000, 10000)
end = time()
print('exe_time: {}[sec]'.format(end - start) + '\n')
