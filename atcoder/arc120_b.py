# https://atcoder.jp/contests/arc120/tasks/arc120_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

MOD = 998244353

def main():
    H, W = map(int, input().split())
    cnt = [[0]*3 for _ in range(H+W)]
    d = {'.':0, 'R':1, 'B':2}
    for i in range(H):
        S = input()
        for j in range(W):
            cnt[i+j][d[S[j]]] += 1
    # print(cnt)
    ans = 1
    for i in range(H+W-1):
        if cnt[i][1]>0 and cnt[i][2]>0:
            print(0)
            return
        if cnt[i][1]==0 and cnt[i][2]==0:
            ans *= 2
            ans %= MOD
    print(ans)
    return

main()


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
