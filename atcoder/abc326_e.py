# https://atcoder.jp/contests/abc326/tasks/abc326_e

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

MOD = 998244353
N = int(input())
A = list(map(int, (input().split())))
invn = pow(N, -1, MOD)

ans = 0
now = invn
for i in range(N):
    ans += now * A[i]
    ans %= MOD
    now += now * invn
    now %= MOD
print(ans)

# print(pow(49, 1, MOD) * pow(9, -1, MOD) % MOD)
# print(pow(49, 1, MOD) * pow(3, -1, MOD) * pow(3, -1, MOD) % MOD)
# print(147 * pow(27, -1, MOD) % MOD)

# ans = 0
# now = pow(N, N-1, MOD)
# for i in range(N):
#     ans += now * A[i]
#     ans %= MOD
#     now += now * invn
#     now %= MOD
# # print(ans)
# for i in range(N):
#     ans *= pow(N, -1, MOD)
#     ans %= MOD
# print(ans)
