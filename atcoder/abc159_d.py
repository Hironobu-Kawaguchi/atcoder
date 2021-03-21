# https://atcoder.jp/contests/abc159/tasks/abc159_d
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

from collections import Counter
N = int(input())
A = list(map(int, (input().split())))
c = Counter(A)
def nC2(n):
    return n*(n-1)//2

all_cnt = 0
for k, v in c.items():
    if v>1:
        all_cnt += nC2(v)

for i in range(N):
    k = c[A[i]]
    ans = all_cnt - nC2(k) + nC2(k-1)
    print(ans)

# S = input()

# N, M = map(int, input().split())
# ans = (N+M)*(N+M-1)//2 - N*M
# print(ans)

# A = [[int(i) for i in input().split()] for _ in range(N)]
