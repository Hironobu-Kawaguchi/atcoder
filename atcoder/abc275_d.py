# https://atcoder.jp/contests/abc275/tasks/abc275_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import heapq
import bisect

N = int(input())
st = set([0])
k = [0]
v = [1]
q = [1]

def f(x):
    ret = 0
    idx = bisect.bisect_right(k, x//2) - 1
    # print(idx, k, v)
    ret += v[idx]
    idx = bisect.bisect_right(k, x//3) - 1
    ret += v[idx]
    return ret

now = heapq.heappop(q)
while now<=N:
    if now in st:
        now = heapq.heappop(q)
        continue
    if now*2 not in st: heapq.heappush(q, now*2)
    if now*3 not in st: heapq.heappush(q, now*3)
    st.add(now)
    k.append(now)
    v.append(f(now))
    now = heapq.heappop(q)

ans = v[bisect.bisect_right(k, N) - 1]
# print(len(v))
print(ans)



# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
