# https://atcoder.jp/contests/arc147/tasks/arc147_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
P = list(map(int, (input().split())))

ans = []

def f(c, i):
    ans.append((c, i+1))
    P[i], P[i+1+ord(c)-ord('A')] = P[i+1+ord(c)-ord('A')], P[i]
    return

# 偶奇が違うところをBで2つずつ前に持ってくる
for i in range(N):
    for j in range(N-2):
        if P[j]%2!=P[j+2]%2 and P[j]%2!=j%2:
            f("B", j)
print(P, file=sys.stderr)
# 偶奇が違うもの同士をAで隣と交換する
for i in range(N-1):
    if P[i]%2!=P[i+1] and P[i]%2==i%2:
        f("A", i)
print(P, file=sys.stderr)
# Bで順番に並べる
for i in range(N):
    for j in range(N-2):
        if P[j]>P[j+2]:
            f("B", j)
print(P, file=sys.stderr)

print(len(ans))
for c, i in ans:
    print(c, i)
