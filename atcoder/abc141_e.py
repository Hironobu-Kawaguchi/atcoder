# https://atcoder.jp/contests/abc141/tasks/abc141_e

# Pypy
N = int(input())
S = input()
DP = [[0]*5005 for _ in range(5005)]

for i in range(N):
    for j in range(N):
        if S[i] == S[j]:
            DP[N-i][N-j] = DP[N-i+1][N-j+1] + 1
ans = 0
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        now = min(DP[i][j], j-i)
        ans = max(ans, now)

print(ans)

# # TLE
# N = int(input())
# S = input()

# ans = 0
# for i in range(N-1):
#     for j in range(i+1+ans, N-ans):
#         for l in range(ans+1, min(j-i, N-j)+1):
#             if S[i:i+l] == S[j:j+l]:
#                 ans = max(ans, l)
#             else:
#                 break

# print(ans)
