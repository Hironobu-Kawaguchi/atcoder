# https://atcoder.jp/contests/abc171/tasks/abc171_f

# import sys
# input = sys.stdin.buffer.readline

MOD = 10**9+7
MAXN = 2*10**6+5
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % MOD)
def nCr(n, r, mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

K = int(input())
S = input()
R = len(S)
N = K + R
ans = 0
for r in range(R,N+1):
    power = pow(25, N-r, MOD)
    ans += nCr(N, r) * power % MOD
    ans %= MOD
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
