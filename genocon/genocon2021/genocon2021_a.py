# https://atcoder.jp/contests/genocon2021/tasks/genocon2021_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


R = {"A": "T",
     "T": "A",
     "C": "G",
     "G": "C",
    }

def reverse_complementary_sequence(s):
    ret = ""
    for a in s:
        ret += R[a]
    return ret

m = int(input())
for i in range(m):
    s = input()
    print(reverse_complementary_sequence(s)[::-1])


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
