# https://atcoder.jp/contests/abc290/tasks/abc290_e
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))

cnt = [0]*(N+1)
ans = [0]
if N%2:
    start = N//2
    cnt[A[N//2]] = 1
    sm = 1
    for i in range(N//2):
        ans.append(ans[-1])
        x1 = start - (i + 1)
        x2 = start + (i + 1)
        if A[x1]!=A[x2]: ans[-1] += 1
        ans[-1] += sm - cnt[A[x1]]
        ans[-1] += sm - cnt[A[x2]]
        cnt[A[x1]] += 1
        cnt[A[x2]] += 1
        sm += 2
        # print(start, x1, x2, ans[-1])
else:
    start = N//2
    sm = 0
    for i in range(N//2):
        ans.append(ans[-1])
        x1 = start - (i + 1)
        x2 = start + i
        if A[x1]!=A[x2]: ans[-1] += 1
        ans[-1] += sm - cnt[A[x1]]
        ans[-1] += sm - cnt[A[x2]]
        cnt[A[x1]] += 1
        cnt[A[x2]] += 1
        sm += 2
        # print(start, x1, x2, ans[-1])

total_ans = 0
for a in ans:
    total_ans += a
print(total_ans)


# ans = 0
# for k in range(1, N):   # j-i
#     for i in range(N-k):
#         cnt = min(i+1, N-(i+k))
#         if A[i]!=A[i+k]:
#             ans += cnt
# print(ans)



# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
