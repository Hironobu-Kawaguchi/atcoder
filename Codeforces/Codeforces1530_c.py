# https://codeforces.com/contest/1530/problem/C

# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    n = int(input())
    a = list(map(int, (input().split())))
    a.sort(reverse=True)
    b = list(map(int, (input().split())))
    b.sort(reverse=True)
    exc = n//4
    st = n - exc
    sum_a = 0
    for i in range(st):
        sum_a += a[i]
    sum_b = 0
    for i in range(st):
        sum_b += b[i]
    mod = n%4
    ans = 0
    mv_cnt = 0
    # print(ans, sum_a, sum_b)
    while sum_a<sum_b:
    # while sum_a<sum_b or ans<40:
        ans += 1
        if (ans+mod)%4==0:   # not increase usuage stages number (a change smallest to 100, b not change)
            mv_cnt += 1
            if mv_cnt<=st:
                sum_a += 100
                sum_a -= a[st-mv_cnt]
        else:                # increase usuage stages number (a add 100, b add next point)
            sum_a += 100
            if ans-mv_cnt<=exc:
                sum_b += b[st-1+ans-mv_cnt]
        # print(ans, sum_a, sum_b)
    print(ans)
    return

t = int(input())
for _ in range(t):
    main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
