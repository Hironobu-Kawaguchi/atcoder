# https://atcoder.jp/contests/arc153/tasks/arc153_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

N = int(input())
S = str(N + 99999)
ans = S[0] + S[0] + S[1:4] + S[3] + S[4:] + S[4]
print(ans)


# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)

# N = int(input())
# N -= 1
# lst = [0] * 6
# for i in range(6):
#     N, tmp = divmod(N, 10)
#     lst[i] = tmp
# lst.reverse()
# # print(lst)
# ans = (lst[0]+1)*110000000 + lst[1]*1000000 + lst[2]*100000 + lst[3]*11000 + lst[4]*101 + lst[5]*10
# print(ans)
