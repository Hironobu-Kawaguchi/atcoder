# Template for AtCoder
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

S = input()
n = int(input())
N, K = map(int, input().split())
l = list(map(int, (input().split())))
A = [[int(i) for i in input().split()] for _ in range(N)]

degree = {'B':'Bachelor', 'M':'Master', 'D':'Doctor'}
l = []
l.append(sum(p))
for i, ai in enumerate(a):
a , mod = divmod((Y - N - 9*i) , 4)
a.sort(reverse=True)
print()

memo = [{} for _ in range(N)]
def dfs(cur, last3):
    if cur == N:
        return 1
    elif last3 in memo[cur]:
        return memo[cur][last3]
    else:
        ret = 0
        ret += dfs(cur + 1, last3[1:] + c)
        memo[cur][last3] = ret
        return ret
print(dfs(0, '   '))

import itertools
for p in itertools.combinations(l, 3):
for p in itertools.product(["7", "5", "3"], repeat = i):

import bisect
b, d = bisect.bisect_right(s, x), bisect.bisect_right(t, x)

import numpy as np
A = np.empty((N, M),dtype=int)
A[n, :] = list(map(int, input().split()))
AB = AB[AB[:, 0].argsort(), :]
X = np.dot(A, B) + C
print(len(X[X>0]))

import heapq
q = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]
s = set()
for n in range(K):
    p, a, b, c = heapq.heappop(q)
    print(-p)
    if a+1 < X and ((a+1, b, c) not in s):
        s.add((a+1, b, c))
        heapq.heappush(q, (-(A[a+1] + B[b] + C[c]), a+1, b, c))

#最大公約数、最小公倍数
import fractions
a,b=map(int, input().split())
f=fractions.gcd(a,b)
f2=a*b//f
print(f,f2)

# フェルマーの小定理
def nCr(n, r, mod=10**9+7):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod
