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

num = np.arange(0,10001,100)
num
df = pd.DataFrame(index=['np_exe_time','nb_exe_time'])

for i in num:
    np_exe_time, nb_exe_time = exe_time_printer(int(i), int(i))
    df[str(i)] = [np_exe_time[:5] + '[sec]', nb_exe_time[:5] + '[sec]']
    
print(df)
