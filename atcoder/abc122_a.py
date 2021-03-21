"""
A - Double Helix
https://atcoder.jp/contests/abc122/tasks/abc122_a
AtCoder 星には四種類の塩基 A, C, G, T が存在し、A と T、C と G がそれぞれ対になります。
文字 b が入力されます。これは A, C, G, T のいずれかです。塩基 b と対になる塩基を表す文字を出力するプログラムを書いてください。
"""
b = input()
d = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
print(d[b])