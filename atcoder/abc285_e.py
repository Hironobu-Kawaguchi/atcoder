# https://atcoder.jp/contests/ABC285/tasks/abc285_e

import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, (input().split())))
B = [0]
for i in range(N-1):
    B.append(B[-1] + A[i//2])
# print(B)

dp = [[0]*N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1):
        dp[i+1][0] = max(dp[i+1][0], dp[i][j] + B[j])
        dp[i+1][j+1] = dp[i][j]
# for i in range(N): print(*dp[i])

ans = 0
for i in range(N):
    ans = max(ans, dp[N-1][i] + B[i])
print(ans)



# WA
# import sys
# input = sys.stdin.buffer.readline

# N = int(input())
# A = list(map(int, (input().split())))

# def f(x):
#     ret = 0
#     n = N - x
#     for i in range(N//2 + 1):
#         cnt = min(n, x*2)
#         ret += A[i] * cnt
#         n -= cnt
#     return ret

# ans = 0
# for i in range(1, N//2 + 1):
#     ans = max(ans, f(i))
#     # print(i, ans)
# print(ans)
