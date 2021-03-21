# https://atcoder.jp/contests/abc167/tasks/abc167_e

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

MOD = 998244353
MAXN = 2*(10**5)+10
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % MOD)
def nCr(n, r, mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod


N, M, K = map(int, input().split())
ans = 0
for i in range(K+1):
    tmp = pow(M-1, N-i-1, MOD) * M % MOD
    tmp *= nCr(N-1,i,MOD)
    ans += tmp % MOD
    ans %= MOD
print(ans)

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
