# https://atcoder.jp/contests/typical90/tasks/typical90_ad

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
cnt = [0]*(N+1)
for i in range(2, N+1):
    if cnt[i]!=0: continue
    for j in range(i, N+1, i):
        cnt[j] += 1

# print(cnt[2:])

ans = 0
for i in range(2, N+1):
    if cnt[i]>=K:
        ans += 1
print(ans)
