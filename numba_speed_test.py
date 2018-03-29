import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time
from numba import jit

def jit_off(num):
    '''
    numbaを使わない方の関数です。
    '''
    result = float(0)
    X = np.random.rand(freq)
    Y = np.random.rand(freq)
    for x in X:
        for y in Y:
            result += x - y

    return result

@jit
def jit_on(freq):
    '''
    numbaを使う方の関数です。
    '''
    result = float(0)
    X = np.random.rand(freq)
    Y = np.random.rand(freq)
    for x in X:
        for y in Y:
            result += x - y

    return result

def exe_time_printer(freq):
    '''
    2つの関数に係数freq(実行回数=freq**2)を引き渡してそれぞれの実行時間を10進数のstr型で出力する関数です。
    '''
    np.set_printoptions(precision=8, suppress=True)

    start = time()
    jit_off(freq)
    exe_time_jit_off = time() - start


    start = time()
    jit_on(freq)
    exe_time_jit_on = time() - start

    # return "%.10f"%exe_time_jit_off, "%.10f"%exe_time_jit_on
    return exe_time_jit_off.astype(np.float), exe_time_jit_on.astype(np.float)

frequency = np.arange(0, 10001, 100)
df = pd.DataFrame(columns=['freq','exe_time_jit_off','exe_time_jit_on'])

for freq in frequency:
    print(freq)
    exe_time_jit_off, exe_time_jit_on = exe_time_printer(freq)
    se = pd.Series([freq, exe_time_jit_off, exe_time_jit_on], index=df.columns)
    df = df.append(se, ignore_index=True)

df.to_csv('result/result.tsv', sep='\t', index=False)
df.plot(x='freq', y=['exe_time_jit_off', 'exe_time_jit_on'], colormap='jet', marker='.', markersize=10, title='Numba Speed Test', figsize=(10,5), alpha=0.5)

plt.savefig('result/result.png')
plt.pause(5)
