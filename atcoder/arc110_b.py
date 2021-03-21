# https://atcoder.jp/contests/arc110/tasks/arc110_b
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)
# import math

base = '110'

def chk(text):
    res = False
    for i in range(3):
        for j, x in enumerate(text):
            if x != base[(j+i)%3]:
                break
        else:
            res = True
    return res

N = int(input())
T = input()

ans = 10**10
if T=='1':
    ans *=2
elif T=='0' or T=='11' or T=='10':
    next
# elif T=='01':
#     ans -= 1
elif chk(T):
    if T[0]=='0':
        ans -= (N+1)//3
    elif T[:2]=='10':
        ans -= N//3
    else:
        ans -= (N-1)//3
else:
    ans = 0
print(ans)

# def main():
#     n = int(input())
#     for a in range(1,38):
#         for b in range(1,26):
#             if pow(3,a) + pow(5,b) == n:
#                 print(a, b)
#                 return
#     print(-1)
#     return

# main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
