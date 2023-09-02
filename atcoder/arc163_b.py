# https://atcoder.jp/contests/arc163/tasks/arc163_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001001001

N, M = map(int, input().split())
A = list(map(int, (input().split())))
B = A[2:]
B.sort()

ans = INF
for i in range(N-2-M+1):
    tmp = max(0, A[0] - B[i]) + max(0, B[i+M-1] - A[1])
    ans = min(ans, tmp)
print(ans)


# WA
# import bisect
# from collections import Counter

# def solve(N, A, M):
#     uplist = []
#     for i in range(2, N):
#         uplist.append(A[i])
#     uplist.sort()
#     upkey, upcum = [0], [0]
#     sm = 0
#     for k, v in sorted(Counter(uplist).items()):
#         upkey.append(k)
#         sm += v
#         upcum.append(sm)
#     print(upkey, upcum, file=sys.stderr)

#     def check_cnt(m):
#         max_cnt = 0
#         for i in range(len(upkey)):
#             mm = m
#             # if upkey[i]<m: continue
#             cnt = upcum[i]
#             if upkey[i]>A[1]:
#                 mm -= upkey[i] - A[1]
#             # if A[0]>upkey[i]:
#             #     mm -= A[0] - upkey[i]
#             v = A[0] - mm
#             if v>0:
#                 idx = bisect.bisect_right(upkey, v) - 1
#                 cnt -= upcum[idx]
#             max_cnt = max(max_cnt, cnt)
#             # print(i, upkey[i], m, mm, v, cnt, max_cnt, file=sys.stderr)
#         return max_cnt

#     l, r = 0, 10**9
#     while l+1<r:
#         m = (l+r)//2
#         max_cnt = check_cnt(m)
#         # print(max_cnt, M, l, r, m, file=sys.stderr)
#         if max_cnt>=M:
#             r = m
#         else:
#             l = m
#     # print(max_cnt, M, l, r, m, file=sys.stderr)
#     # print(check_cnt(l), file=sys.stderr)
#     if check_cnt(l)>=M:
#         return l
#     else:
#         return r

# def main():
#     N, M = map(int, input().split())
#     A = list(map(int, (input().split())))
#     # if A[0]>A[1]:
#     #     dif = A[0]-A[1]
#     #     cand = set()
#     #     for i in range(2, N):
#     #         if A[i]<=A[i]<=A[0]:
#     #             cand.add(A[i])
#     #     ans = 10**9
#     #     for x in cand:
#     #         A[0], A[1] = x, x
#     #         ans = min(ans, solve(N, A, M) + dif)
#     # else:
#     #     ans = solve(N, A, M)
#     ans = solve(N, A, M)
#     print(ans)
#     return

# main()
