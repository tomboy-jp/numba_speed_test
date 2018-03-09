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

    start = time()
    numpy_only(x, y)
    np_exe_time = time() - start

    start = time()
    numba_jit(x, y)
    nb_exe_time = time() - start

    return "%.10f"%np_exe_time, "%.10f"%nb_exe_time

li = [1, 10, 100, 1000, 10000]
df = pd.DataFrame(index=['np_exe_time','nb_exe_time'])

for i in li:
    np_exe_time, nb_exe_time = exe_time_printer(i, i)
    df[str(i)] = [np_exe_time + '[sec]', nb_exe_time + '[sec]']

print(df)
