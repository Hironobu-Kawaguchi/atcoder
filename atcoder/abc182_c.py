# https://atcoder.jp/contests/abc182/tasks/abc182_c
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
def main():
    N = input()
    cnt = [0]*3
    sumn = 0
    for s in N:
        i = int(s) % 3
        cnt[i] += 1
        sumn += i
    mod = sumn%3
    if mod==0:
        ans = 0
    elif mod==1:
        if cnt[1]>=1:
            ans = 1
        elif cnt[2]>=2:
            ans = 2
        else:
            ans = 0
    else:
        if cnt[2]>=1:
            ans = 1
        elif cnt[1]>=2:
            ans = 2
        else:
            ans = 0
    if ans == len(N):
        ans = -1
    print(ans)
    return

main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
