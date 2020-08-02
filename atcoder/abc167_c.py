# https://atcoder.jp/contests/abc167/tasks/abc167_c

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

INF = 1001001001
N, M, X = map(int, input().split())
C, A = [], []
for i in range(N):
    _c = list(map(int, (input().split())))
    _a = _c[1:]
    _c = _c[0]
    A.append(_a)
    C.append(_c)
ans = INF
for b in range(1<<N):
    money = 0
    point = [0]*M
    for i in range(N):
        if (b>>i)&1:
            money += C[i]
            for j in range(M):
                point[j] += A[i][j]
    for j in range(M):
        if point[j] < X:
            break
    else:
        ans = min(ans, money)
if ans == INF:
    print(-1)
else:
    print(ans)


# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
