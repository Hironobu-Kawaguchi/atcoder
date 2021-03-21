# D - 756
# https://atcoder.jp/contests/abc114/tasks/abc114_d
"""
整数 N が与えられます。
N! (=1×2×...×N) の約数のうち、七五数 は何個あるでしょうか？
ここで、七五数とは約数をちょうど 75 個持つ正の整数です。
"""

N = int(input())
e = [0] * (N+1)
for i in range(2, N+1):
    cur = i
    for j in range(2, i+1):
        while cur % j == 0:
            e[j] += 1
            cur //= j
def num(m): # e の要素のうち m-1 以上のものの個数
    return len(list(filter(lambda x: x >= m-1, e)))
print(num(75) + num(25) * (num(3) - 1) + num(15) * (num(5) - 1)
    + num(5) * (num(5) - 1) * (num(3) - 2) // 2)
