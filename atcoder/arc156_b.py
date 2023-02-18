# https://atcoder.jp/contests/arc156/tasks/arc156_b

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

MAXN = 5 * 10**5
fact = [1]
ifact = [1]
for i in range(MAXN):
    fact.append(fact[-1] * (i+1) % MOD)
    ifact.append(pow(fact[-1], MOD-2, MOD))
def nCr(n, r):
    return fact[n] * ifact[r] * ifact[n-r] % MOD

N, K = map(int, input().split())
A = list(map(int, (input().split())))
st = set(A)

mex_list = []
cnt = 0
now = 0
while cnt<K+1:
    if now not in st:
        mex_list.append(now)
        cnt += 1
        st.add(now)
    now += 1
# print(mex_list)

ans = 0
for i in range(K+1):
    if i==0 and mex_list[i]==0: continue
    r = K - i
    ans += nCr(mex_list[i] + r - 1, r)
    ans %= MOD
    # print(i, mex_list[i], r, ans)
print(ans)



# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
