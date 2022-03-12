# https://atcoder.jp/contests/abc241/tasks/abc241_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    S = []
    for i in range(N):
        s = input()
        S.append(s)
    # print(S)
    for i in range(N-5):
        for j in range(N):
            cnt = 0
            for k in range(6):
                if S[i+k][j]=='#': 
                    cnt += 1
            if cnt>=4:
                print("Yes")
                return
    for i in range(N):
        for j in range(N-5):
            cnt = 0
            for k in range(6):
                if S[i][j+k]=='#': 
                    cnt += 1
            # print(i,j,cnt)
            if cnt>=4:
                print("Yes")
                return
    for i in range(N-5):
        for j in range(N-5):
            cnt = 0
            for k in range(6):
                if S[i+k][j+k]=='#': 
                    cnt += 1
            if cnt>=4:
                print("Yes")
                return
    for i in range(5, N):
        for j in range(N-5):
            cnt = 0
            for k in range(6):
                if S[i-k][j+k]=='#': 
                    cnt += 1
            if cnt>=4:
                print("Yes")
                return
    print("No")
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
