# https://atcoder.jp/contests/arc121/tasks/arc121_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

import bisect

def main():
    N = int(input())
    lst = [[] for _ in range(3)]
    for i in range(2*N):
        a, c = input().split()
        a = int(a)
        if c=='R':
            lst[0].append(a)
        elif c=='G':
            lst[1].append(a)
        else:
            lst[2].append(a)
    # print(lst)

    odd = []
    for i in range(3):
        if len(lst[i])%2:
            odd.append(i)
    # print(odd)

    if len(odd)==0:
        print(0)
        return
    lst[odd[0]].sort()
    lst[odd[1]].sort()
    evenidx = list(set(range(3)) - set(odd))[0]
    lst[evenidx].sort()
    ans = 1001001001001001
    for ai in lst[odd[1]]:
        j = bisect.bisect_left(lst[odd[0]], ai)
        if j!=0:
            ans = min(ans, abs(ai - lst[odd[0]][j-1]))
        if j!=len(lst[odd[0]]):
            ans = min(ans, abs(ai - lst[odd[0]][j]))
    if len(lst[evenidx])>0:  # 偶数個の色
        even0 = []
        for i, ai in enumerate(lst[evenidx]):
            diff = 1001001001001001
            j = bisect.bisect_left(lst[odd[0]], ai)
            if j!=0:
                diff = min(diff, abs(ai - lst[odd[0]][j-1]))
            if j!=len(lst[odd[0]]):
                diff = min(diff, abs(ai - lst[odd[0]][j]))
            even0.append((diff, i))
        even0.sort()
        even1 = []
        for i, ai in enumerate(lst[evenidx]):
            diff = 1001001001001001
            j = bisect.bisect_left(lst[odd[1]], ai)
            if j!=0:
                diff = min(diff, abs(ai - lst[odd[1]][j-1]))
            if j!=len(lst[odd[1]]):
                diff = min(diff, abs(ai - lst[odd[1]][j]))
            even1.append((diff, i))
        even1.sort()
        if even0[0][1]!=even1[0][1]:
            ans = min(ans, even0[0][0] + even1[0][0])
        else:
            ans = min(ans, even0[0][0] + even1[1][0])
            ans = min(ans, even0[1][0] + even1[0][0])

    print(ans)
    return

main()

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
