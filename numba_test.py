import numpy as np
import pandas as pd
from time import time
from numba import jit

def numpy_only(x_num, y_num):

    result = float(0)
    X = np.random.rand(x_num)
    Y = np.random.rand(y_num)
    for x in X:
        for y in Y:
            result += x - y

    return result

@jit
def numba_jit(x, y):

    result = float(0)
    X = np.random.rand(x)
    Y = np.random.rand(y)
    for x in X:
        for y in Y:
            result += x - y

    return result

def exe_time_printer(x, y):

    print('x = ' + str(x) + ', y = ' + str(y) + '\n')
    print('numpy_only, start!')
    start = time()
    numpy_only(x, y)
    np_exe_time = time() - start
    print('exe_time: {}[sec]'.format(np_exe_time) + '\n')

    print('numba_jit, start!')
    start = time()
    numba_jit(x, y)
    nb_exe_time = time() - start
    print('exe_time: {}[sec]'.format(nb_exe_time) + '\n')

    return np_exe_time, nb_exe_time

li = [1, 10, 100, 1000, 10000]
df = pd.DataFrame(index=['np_exe_time','nb_exe_time'])

for i in li:
    np_exe_time, nb_exe_time = exe_time_printer(i, i)
    df[str(i)] = [str(np_exe_time) + '[sec]', str(nb_exe_time) + '[sec]']

print(df)
