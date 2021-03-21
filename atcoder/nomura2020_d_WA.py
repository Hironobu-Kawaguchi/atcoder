# https://atcoder.jp/contests/nomura2020/tasks/nomura2020_d
import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 10**9+7
from itertools import product

N = int(input())
P = list(map(int, (input().split())))
s = set()
# g = [[] for _ in range(N)]
k = []
for i in range(N):
    if P[i]==-1:
        k.append(i)
    else:
        # g[P[i]-1].append(i)
        if P[i]-1 > i:
            s.add((i,P[i]-1))
        else:
            s.add((P[i]-1,i))
# print(s)
# print(k)
# print(g)

cnt=0
ans = 0
for p in product(range(N-1), repeat=len(k)):
    # print(p)
    ss = set()
    for i, j in enumerate(k):
        # if p[i] == j: break
        if p[i] >= j:
            ss.add((j,p[i]+1))
        else:
            ss.add((p[i],j))
    else:
        ans += len(s | ss)
        ans %= MOD
        cnt += 1
print(ans)
print(cnt, (N-1)**len(k))


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
