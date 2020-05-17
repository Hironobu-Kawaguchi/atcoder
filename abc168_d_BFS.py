# https://atcoder.jp/contests/abc168/tasks/abc168_d

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from collections import deque
N,M = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

ans = [-1]*N
ans[0] = 0
q = deque([0])    # 今の部屋

while q:
    now =  q.popleft()
    for nxt in g[now]:
        if ans[nxt] == -1:
            ans[nxt] = now
            q.append(nxt)
print('Yes')
for i in range(1,N):
    print(ans[i]+1)

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
