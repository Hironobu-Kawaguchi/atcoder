# https://atcoder.jp/contests/abc323/tasks/abc323_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import heapq

N = int(input())
cnt = dict()
hq = []
for _ in range(N):
    s, c = map(int, input().split())
    cnt[s] = c
    heapq.heappush(hq, s)

ans = 0
while hq:
    s = heapq.heappop(hq)
    c = cnt[s]
    # print(s, c, file=sys.stderr)
    if c <2: continue
    union = c//2
    cnt[s] -= union*2
    if s*2 > 10**9:
        b = bin(c)[2:]
        # print(b, file=sys.stderr)
        ans += b[:-1].count('1')
        cnt[s] = int(b[-1])
    elif s*2 not in cnt:
        cnt[s*2] = union
        heapq.heappush(hq, s*2)
    else:
        cnt[s*2] += union

for k, v in sorted(cnt.items()):
    # print(k, v, file=sys.stderr)
    ans += v

print(ans)
