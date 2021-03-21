# https://atcoder.jp/contests/abc156/tasks/abc156_e

import sys
input = sys.stdin.buffer.readline
MOD = 10**9+7

MAXN = 2*10**5+5
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % MOD)
def nCr(n, r, mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

n, k = map(int, (input().split()))
ans = 0
for m in range(min(n-1,k)+1):
    ans += nCr(n,m) * nCr(n-1, n-m-1) % MOD
    ans %= MOD
print(ans)


# s = set([tuple([1]*n)])
# # print(s)

# for _ in range(k):
#     nexts = set()
#     for t in list(s):
#         for i in range(n):
#             for j in range(n):
#                 lst = list(t)
#                 if i == j: continue
#                 if lst[i] == 0: continue
#                 lst[i] -= 1
#                 lst[j] += 1
#                 nexts.add(tuple(lst))
#     s = nexts
#     # print(s)

# ans = len(s) % MOD
# # print(s)
# print(ans)
