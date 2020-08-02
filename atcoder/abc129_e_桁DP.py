# https://atcoder.jp/contests/abc129/tasks/abc129_e
# import sys
# # input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

MOD = 10**9 + 7
L = input()
n = len(L)
dp1 = [0] * (n+1)   # == L の組み合わせ
dp2 = [0] * (n+1)   #  < L の組み合わせ
dp1[0] = 1

for i in range(n):
    if L[i] == '1':
        dp1[i+1] = (dp1[i] * 2) % MOD
        dp2[i+1] = (dp1[i] + dp2[i] * 3) % MOD
    else:
        dp1[i+1] = dp1[i]
        dp2[i+1] = (dp2[i] * 3) % MOD
print((dp1[n] + dp2[n])%MOD)
