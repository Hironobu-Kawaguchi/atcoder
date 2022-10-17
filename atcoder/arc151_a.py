# https://atcoder.jp/contests/arc151/tasks/arc151_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    S = input()
    T = input()

    cnt_s, cnt_t = 0, 0
    for i in range(N):
        if S[i]=='1': cnt_s += 1
        if T[i]=='1': cnt_t += 1
    if (cnt_s%2)!=(cnt_t%2):
        print(-1)
        return
    ans = ['0']*N
    diff = cnt_s - cnt_t
    flg = 1 if diff>=0 else -1
    idx = N-1
    while diff!=0:
        # print(idx, diff)
        if int(S[idx])-int(T[idx])==flg:
            ans[idx] = '1'
            diff -= flg * 2
        idx -= 1
    print(''.join(ans))
    return

main()


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
