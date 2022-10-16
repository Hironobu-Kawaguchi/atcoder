# https://atcoder.jp/contests/abc273/tasks/abc273_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

Q = int(input())
notes = {}
qs = [-1]
to = [0]
now = 0
ans = []
for qi in range(Q):
    query = input()
    if query[:3]=='ADD':
        x = int(query[4:])
        to.append(now)
        qs.append(x)
        now = len(qs) - 1
    elif query[:4]=='SAVE':
        y = int(query[5:])
        notes[y] = now
    elif query[:4]=='LOAD':
        z = int(query[5:])
        if z in notes:
            now = notes[z]
        else:
            now = 0
    else:
        now = to[now]
    ans.append(qs[now])
print(*ans)




# import copy

# Q = int(input())
# notes = {}
# A = []
# ans = []
# for qi in range(Q):
#     query = input()
#     if query[:3]=='ADD':
#         x = int(query[4:])
#         A.append(x)
#     elif query[:4]=='SAVE':
#         y = int(query[5:])
#         notes[y] = copy.copy(A)
#     elif query[:4]=='LOAD':
#         z = int(query[5:])
#         if z in notes:
#             A = copy.copy(notes[z])
#         else:
#             A = []
#     else:
#         if len(A)!=0:
#             A.pop()
#     if len(A)==0:
#         ans.append(-1)
#     else:
#         ans.append(A[-1])
# print(*ans)


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
