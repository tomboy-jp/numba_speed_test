# numba Speed Test  
numbaモジュールを使って関数を雑に高速化します。  
## numbaとは  
[公式](https://numba.pydata.org/)によるとPythonインタプリタを切り替えることなくC、C ++、Fortranと同様にJIT(Just In Time)コンパイルできる、とのこと。  
import時にLLVMコンパイラなるもので最適化したコードを生成してくれるそうです。  
実装方法もCythonみたいな初心者殺しではなく、importして関数の上に一行「@jit」と書くだけ。  
(デコレータ機能で関数ごと高次関数に引き渡している模様)  
ここまで聞くと低級言語のレゾンデートルを破壊しかねないアトモスフィアを醸し出しているけれど、残念ながら扱える機能に制限がある模様。  
ざっと読んだ限りで大雑把に述べるとstr型がダメでint, float, boolあたりはOK。  
配列やタプルは大体大丈夫だけど、dicとsetは無理みたい。  
数字に強いのでnumpyも幅広くサポートしているみたいでモジュール内で「import numpy」をgrepしたら40件返ってきた。  
(ダメ元でpandasでもやってみたけど見事に0件だった)  
もっと知りたいときは公式の[リファレンスマニュアル](http://numba.pydata.org/numba-doc/0.37.0/reference/index.html)から。

## 実験内容
試験に使ったコードは[こちら](https://github.com/tomboy-jp/numba_speed_test/blob/master/numba_test.py)。  
コア部分を抽出すると、  
```
result = float(0)
X = np.random.rand(x_num)
Y = np.random.rand(y_num)
for x in X:
    for y in Y:
        result += x - y

return result
```
といった感じのシンプルなもの。
jitデコレータなしの関数とjitデコレータ付きの関数を用意し、
x_numとy_numの値を変更しながら(今回はx_num = y_num)、それぞれの実行時間を計測してみた。  

## 実験結果

![実行結果](https://raw.githubusercontent.com/tomboy-jp/numba_speed_test/master/result/result.png "実行結果")

x軸がx_numとy_numの値でy軸が実行時間(sec)を示している。
青いグラフがnumpyだけの(jitデコレータなしの)実験結果で、赤いグラフがnumbaを使った実験結果である。  
うん、numba圧勝としか言えない。  
初回(0件で投げたとき)こそ惜敗しているものの(読み込みの時間かと)、その後はどんどん差をつけて最終的にはjitなしをフルボッコにしている。  
他の言語の速度試験をしたことがないので、上には上がいるのかもしれないけど、コスパ(効果/学習コスト)がすごい。  
Pythonっ子としては大変有益な情報だった。  
