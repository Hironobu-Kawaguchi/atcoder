# https://atcoder.jp/contests/arc124/tasks/arc124_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
a = list(map(int, (input().split())))
b = list(map(int, (input().split())))
b_set = set(b)
ans_set = set()
for i in range(N):
    ans_set.add(a[i]^b[0])
# print(ans_set)
for i in range(N):
    for c in list(ans_set):
        d = a[i]^c
        if d not in b_set:
            # print('remove', i, c, d)
            ans_set.remove(c)
ans = list(ans_set)
ans.sort()
print(len(ans))
for x in ans:
    print(x)


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
