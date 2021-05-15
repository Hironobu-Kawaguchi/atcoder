# https://atcoder.jp/contests/abc201/tasks/abc201_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# no, nq = 0, 0
# for c in S:
#     if c=='o':
#         no += 1
#     elif c=='?':
#         nq += 1
# print(no, nq)

S = input()

def check(num):
    cnt = [0]*10
    for _ in range(4):
        cnt[num%10] += 1
        num //= 10
    for i in range(10):
        if S[i]=='o':
            if cnt[i]==0:
                return False
        elif S[i]=='x':
            if cnt[i]>0:
                return False
    return True

ans = 0
for i in range(10000):
    if check(i):
        # print(i)
        ans += 1

print(ans)

# ans = 1
# for i in range(no):
#     ans *= 4-i
# for i in range(4-no):
#     ans *= nq-i
# for i in range(4-no):
#     ans //= i+1
# print(ans)

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
