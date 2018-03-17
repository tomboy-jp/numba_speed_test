import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time
from numba import jit
import sys

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

freq = np.arange(0,10001,1000)
df = pd.DataFrame(columns=['freq','np_exe_time','nb_exe_time'])

for i in freq:
    print(i)
    np_exe_time, nb_exe_time = exe_time_printer(int(i), int(i))
    se = pd.Series([i, float(np_exe_time[:7]), float(nb_exe_time[:7])], index=df.columns)
    df = df.append(se, ignore_index=True)

df.to_csv('result/result.tsv', sep='\t', index=False)
df.plot(x='freq', y=['np_exe_time', 'nb_exe_time'], colormap='jet', marker='.', markersize=10, title='Numba Speed Test', figsize=(10,5), alpha=0.5)
plt.savefig('result/result.png')
plt.pause(5)
