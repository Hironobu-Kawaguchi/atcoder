# D - Christmas
# https://atcoder.jp/contests/abc115/tasks/abc115_d
"""
とある世界では、今日はクリスマスです。
高羽氏のパーティで、彼は多次元バーガーを作ることにしました。レベル L バーガー (L は 0 以上の整数) とは次のようなものです。
レベル 0 バーガーとは、パティ 1 枚である。
レベル L バーガー (L≥1) とは、バン 1 枚、レベル L−1 バーガー、パティ 1 枚、レベル L−1 バーガー、バン 1 枚、をこの順に下から積み重ねたものである。
例えば、パティを P、バンを B で表すと、レベル 1 バーガーは BPPPB (を 90 度回転したもの)、レベル 2 バーガーは BBPPPBPBPPPBB といった見た目になります。
高羽氏が作るのはレベル N バーガーです。
ダックスフンドのルンルンは、このバーガーの下から X 層を食べます (パティまたはバン 1 枚を 1 層とします)。
ルンルンはパティを何枚食べるでしょうか？
"""
"""
N, X = map(int, input().split())
a, p = [1], [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)
def f(N, X): # X <= 0 や X > a_N を許容し解説本文から簡略化
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N-1]:
        return f(N-1, X-1)
    else:
        return p[N-1] + 1 + f(N-1, X-2-a[N-1])
print(f(N, X))
print()
"""
N, X = map(int, input().split())
a = [2**(i+2) - 3 for i in range(N+1)]  # 層の数
p = [2**(i+1) - 1 for i in range(N+1)]  # パティの数
def f(N, X):
    if N == 0:
        return 1 if X > 0 else 0
    elif X <= 1 + a[N-1]:
        return f(N-1, X-1)
    else:
        return p[N-1] + 1 + f(N-1, X-2-a[N-1])
print(f(N, X))
