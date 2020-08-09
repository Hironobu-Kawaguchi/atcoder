"""
B - 754
https://atcoder.jp/contests/abc114/tasks/abc114_b
数字 1, 2, ..., 9 からなる文字列 S があります。 ダックスフンドのルンルンは、S から連続する 3 個の数字を取り出し、 1 つの整数 X としてご主人様の元に持っていきます。
（数字の順番を変えることはできません。）
ご主人様が大好きな数は 753 で、これに近い数ほど好きです。 
X と 753 の差（の絶対値）は最小でいくつになるでしょうか？
 """
S = input()
l = len(S)
X = []
for i in range(l-2):
    X.append(abs(int(S[i:i+3]) - 753))
print(min(X))