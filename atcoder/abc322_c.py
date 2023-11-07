# https://atcoder.jp/contests/abc322/tasks/abc322_c

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, input().split()))

hanabi = [False] * N
for i in range(M):
    hanabi[A[i]-1] = True
ans = [0] * N
for i in range(N-1, -1, -1):
    if hanabi[i]:
        ans[i] = 0
    else:
        ans[i] = ans[i+1] + 1
for i in range(N):
    print(ans[i])
