"""
C - GeT AC
https://atcoder.jp/contests/abc122/tasks/abc122_c
A, C, G, T からなる長さ N の文字列 S が与えられます。以下の Q 個の問いに答えてください。
問 i (1≤i≤Q): 整数 li,ri (1≤li<ri≤N) が与えられる。
S の先頭から li 文字目から ri 文字目までの (両端含む) 部分文字列を考える。
この文字列に AC は部分文字列として何回現れるか。
"""
N, Q = map(int, input().split())
S = input()
t = [0] * (N + 1)
for i in range(N):
    t[i + 1] = t[i] + (1 if S[i : i + 2] == 'AC' else 0)
for i in range(Q):
    l, r = map(int, input().split())
    print(t[r-1] - t[l-1])
"""
N, Q = map(int, input().split())
S = input()
for _ in range(Q):
    l, r = map(int, input().split())
    print(S[l-1:r].count('AC'))
"""