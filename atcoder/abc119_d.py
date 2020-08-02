"""
D - Lazy Faith
https://atcoder.jp/contests/abc119/tasks/abc119_d
東西方向に伸びる道路に沿って A 社の神社と B 軒の寺が建っています。 
西から i 社目の神社は道路の西端から si メートルの地点に、西から i 軒目の寺は道路の西端から ti メートルの地点にあります。
以下の Q 個の問いに答えてください。
問 i (1≤i≤Q): 道路の西端から xi メートルの地点から出発して道路上を自由に移動するとき、神社一社と寺一軒を訪れるのに必要な最小の移動距離は何メートルか？ 
(必要数を超えた数の寺社を通過してもよい。)
"""
import bisect
A, B, Q = map(int, input().split())
INF = 10 ** 18
s = [-INF] + [int(input()) for i in range(A)] + [INF]
t = [-INF] + [int(input()) for i in range(B)] + [INF]
for q in range(Q):
    x = int(input())
    b, d = bisect.bisect_right(s, x), bisect.bisect_right(t, x)
    res = INF
    for S in [s[b - 1], s[b]]:
        for T in [t[d - 1], t[d]]:
            d1, d2 = abs(S - x) + abs(T - S), abs(T - x) + abs(S - T)
            res = min(res, d1, d2)
    print(res)