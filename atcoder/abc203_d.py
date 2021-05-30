# https://atcoder.jp/contests/abc203/tasks/abc203_d

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]
lim = (K*K)//2 + 1
ng, ok = -1, 10**10  # case 0 is ok

while ng+1 < ok:
    mid = (ng + ok)//2
    cum = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            cum[i+1][j+1] = cum[i+1][j] + cum[i][j+1] - cum[i][j]
            if A[i][j] > mid:
                cum[i+1][j+1] += 1
    ext = False
    for i in range(N-K+1):
        for j in range(N-K+1):
            if cum[i+K][j+K] - cum[i+K][j] -cum[i][j+K] + cum[i][j] < lim:
                ext = True
                break
    if ext: ok = mid
    else:   ng = mid

print(ok)

# # TLE
# import numpy as np

# N, K = map(int, input().split())
# A = np.array([[int(i) for i in input().split()] for _ in range(N)])
# # print(A)
# mid = (K*K)//2 + 1
# ans = 1001001001
# for i in range(N-K+1):
#     for j in range(N-K+1):
#         tmp = A[i:i+K, j:j+K]
#         tmp = tmp.flatten()
#         tmp = np.sort(tmp)[::-1]
#         # print(tmp)
#         ans = min(ans, tmp[mid-1])
# print(ans)

