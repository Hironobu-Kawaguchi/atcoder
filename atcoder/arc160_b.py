# https://atcoder.jp/contests/arc160/tasks/arc160_b

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

def main():
    N = int(input())
    M = int(N**0.5)
    ans = 0
    for y in range(1, M+1):
        # x < y < z の場合
        ans += 6 * (y-1) * (N//y - y) % MOD
        ans %= MOD
        # x = y < z の場合
        ans += 3 * (N//y - y) % MOD
        ans %= MOD
        # x < y = z の場合
        ans += 3 * (y-1) % MOD
        ans %= MOD
        # x = y = z の場合
        ans += 1
    ans %= MOD
    print(ans)
    return

T = int(input())
for _ in range(T):
    main()



# def main():
#     N = int(input())
#     M = int(N**0.5)
#     # max(x, y, z) <= M の場合
#     ans = pow(M, 3, MOD)
#     # max(x, y, z) > M の場合
#     for i in range(1, N//(M+1)+1):
#         ans += 3 * ((N//i - N//(i+1))) * (i**2) % MOD
#         ans %= MOD
#     print(ans)
#     return

# T = int(input())
# for _ in range(T):
#     main()
