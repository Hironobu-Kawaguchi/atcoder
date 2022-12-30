# https://atcoder.jp/contests/ABC283/tasks/abc283_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import copy

S = input()
N = len(S)
lst = [set()]
now = 0
ans = "Yes"
for c in S:
    if c=='(':
        now += 1
        lst.append(copy.copy(lst[now-1]))
    elif c==')':
        now -= 1
        lst.pop()
    else:
        # print(c, now, lst[now])
        if c in lst[now]:
            ans = "No"
            break
        lst[now].add(c)

print(ans)


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
