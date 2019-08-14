# https://atcoder.jp/contests/abc053/tasks/arc068_b

N = int(input())
A = list(map(int, input().split()))
s = set(A)
k = len(s)
if k % 2:
    ans = k
else:
    ans = k - 1
print(ans)


# N = int(input())
# A = list(map(int, input().split()))
# MAX_A = 10**5
# dp = [0] * (MAX_A + 1)
# for i in range(N):
#     dp[A[i]] += 1

# tmp = 0
# for j in range(MAX_A + 1):
#     if dp[j] > 0:
#         tmp += dp[j] - 1
# tmp += tmp % 2
# print(N - tmp)