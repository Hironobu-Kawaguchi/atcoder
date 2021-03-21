"""
B - ATCoder
https://atcoder.jp/contests/abc122/tasks/abc122_b
英大文字からなる文字列 S が与えられます。
S の部分文字列 (注記を参照) であるような最も長い ACGT 文字列 の長さを求めてください。
ここで、ACGT 文字列とは A, C, G, T 以外の文字を含まない文字列です。
"""
"""
S = input()
N = len(S)
ans = 0
for i in range(N):
    for j in range(i, N):
        if all('ACGT'.count(c) == 1 for c in S[i : j + 1]):
            ans = max(ans, j - i + 1)
print(ans)
"""
S = input()
L = ['A', 'T', 'C', 'G']
n, num = 0, 0
for s in S:
    if s in L:
        n += 1
    else:
        num = max(num, n)
        n = 0
num = max(num, n)
print(num)