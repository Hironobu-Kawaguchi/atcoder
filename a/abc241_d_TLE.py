# https://atcoder.jp/contests/abc241/tasks/abc241_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import array
import bisect

def main():
    Q = int(input())
    A = array.array('q')
    for qi in range(Q):
        q = input()
        if q[0]=='1':
            t, x = map(int, q.split())
            bisect.insort(A, x)
        elif q[0]=='2':
            t, x, k = map(int, q.split())
            idx = bisect.bisect_right(A, x)
            if idx<k:
                print(-1)
            else:
                print(A[idx-k])
        else:
            t, x, k = map(int, q.split())
            idx = bisect.bisect_left(A, x)
            if idx>len(A)-k:
                print(-1)
            else:
                print(A[idx+k-1])
    return

main()


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
