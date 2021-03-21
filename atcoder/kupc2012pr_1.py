# https://atcoder.jp/contests/kupc2012pr/tasks/kupc2012pr_1

import sys
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())

def a(m, n):
    """
    アッカーマン関数
    m <= 3, n <= 60
    """
    if m == 0:
        return n + 1
    if m == 1:
        return n + 2
    if m == 2:
        return 2*n + 3
    if m == 3:
        return pow(2, n+3) - 3

print(a(m, n))
