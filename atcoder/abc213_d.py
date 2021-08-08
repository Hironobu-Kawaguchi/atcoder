# https://atcoder.jp/contests/ABC213/tasks/abc213_d

import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
to = [[] for _ in range(N)]
gone = [False] * N
gone[0] = True

for i in range(N-1):
    A, B = map(int, input().split())
    to[A-1].append(B-1)
    to[B-1].append(A-1)
for i in range(N):
    to[i].sort()
# print(to)

ans = []

def dfs(now):
    gone[now] = True
    ans.append(now+1)
    for next in to[now]:
        if gone[next]: continue
        dfs(next)
        ans.append(now+1)
    if now==0: return
    return

dfs(0)
print(*ans)
