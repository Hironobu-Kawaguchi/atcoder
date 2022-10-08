# https://atcoder.jp/contests/abc271/tasks/abc272_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, (input().split())))

vals = [set() for _ in range(M+1)]
for i in range(N):
    if A[i]>N: continue
    l = 1 if A[i]>=0 else (-A[i]+i)//(i+1)
    r = min(M, (N-A[i]-1)//(i+1))
    for j in range(l, r+1):
        vals[j].add(A[i] + (i+1)*j)

for j in range(1,M+1):
    lst = sorted(list(vals[j]))
    # print(j, lst)
    exi = [False]*(len(lst)+1)
    for v in lst:
        if v<len(lst): exi[v] = True
    ans = 0
    while exi[ans]: ans += 1
    print(ans)


# rest = set(range(M))
# ans = [-1]*M
# now = 0
# while rest:
#     chk = [-1]*(M+1)
#     for i in range(N):
#         if now>A[i] and (now-A[i])%(i+1)==0:
#             tmp = (now-A[i])//(i+1)
#             if tmp<=M:
#                 chk[tmp] = now
#     for j in list(rest):
#         if chk[j+1]==-1:
#             ans[j] = now
#             rest.remove(j)
#     # print(now, chk, ans)
#     now += 1
# for j in range(M):
#     print(ans[j])

