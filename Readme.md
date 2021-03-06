# numba Speed Test  
numbaモジュールを使って関数を雑に高速化します。  
## numbaとは  
特定条件下でPythonの実行速度を超絶高速化するモジュールです。  
[公式](https://numba.pydata.org/)によるとPythonインタプリタを切り替えることなくC、C ++、Fortranと同様に  
JIT(Just In Time)コンパイルできる、とのこと。  
import時にLLVM(Low Level Virtual Machine)コンパイラで最適化したコードを生成してくれるそうです。  
素晴らしい。  

## 実装方法
numbaの強みは実装の手軽さにある。  
importして関数の上に一行「@jit」と書くだけ。  
本当にそれだけで早くなるのだから驚きである。  
それも低級言語に肉薄するレベルで早くなるらしい。  
(デコレータ機能で対象の関数ごと高次関数に引き渡し、その高次関数がC(or C++?)を呼び出して処理している模様)  
Cythonと格闘していた時間を返せと言いたい。     

ここまで簡単だと逆に何か裏があるのではと疑ってしまうが、そこは安心して構わない。  
しっかりと裏がある。  

## numbaの限界  
このnumba、扱える機能に結構な制限がある。  
ざっくり言うと対象の関数に文字列型が入った途端まったく速度が出なくなる。  
どれくらい遅くなるかと言うと普通のPythonに戻っちゃうくらい。  
というかモジュール読み込む時間を考えたらむしろ普通のPythonより遅いまである。   
使いどころ注意報。  

具体的に言うとstr型がダメでint, float, boolあたりはOK。  
配列やタプルは大体大丈夫だけど、dicとsetは無理みたい。  
numpyのことは幅広くサポートしているみたいでモジュール内で「import numpy」をgrepしたら40件返ってきた。  
(ダメ元でpandasでもやってみたけどものの見事に0件だった)  
同じく演算に特化したnumpy同様、実に男らしいモジュールですな。  

より詳しい情報は公式の[リファレンスマニュアル](http://numba.pydata.org/numba-doc/0.37.0/reference/index.html)から。  

## 実験内容
試験に使ったコードは[こちら](https://github.com/tomboy-jp/numba_speed_test/blob/master/numba_speed_test.py)  
計算に使用して居るコア部分は、  
```
result = float(0)
X = np.random.rand(num)
Y = np.random.rand(num)
for x in X:
    for y in Y:
        result += x - y

return result
```
といった感じ。  
実にシンプルですな。  

jitデコレータなしverとjitデコレータverの2つの関数を用意し、  
実行回数を変更しながら、それぞれの実行時間を計測してみた。  

## 実験結果

![実行結果](https://raw.githubusercontent.com/tomboy-jp/numba_speed_test/master/result/result.png "実行結果")

x軸がループの回数でy軸が実行時間(sec)を示している。  
青いグラフがjitデコレータなしの実験結果で、赤いグラフがjitデコレータを使った実験結果である。  

みなまで言うまい。    

初回こそnumbaが僅かに出遅れているものの(たぶん読み込みの時間かと)、  
その後はどんどん差をつけて最終的には勝負にならなくなっている。    
一応回を重ねるにつれnumbaの方も実行時間が長くなっているんだけど、文字通りの桁違いってやつでして。  
これでも他の低級言語に比べちゃまだまだ遅いんだろうけど、numbaはコスパ(効果/学習コスト)がすごいと思いました。  

しかし、やれることに結構な制限があるので、いつかはCythonやJuliaあたりを試したい。
