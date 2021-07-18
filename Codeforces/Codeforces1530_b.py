# https://codeforces.com/contest/1530/problem/B

# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)


def main():
    h, w = map(int, input().split())
    ans = []
    for i in range(h):
        line = ''
        for j in range(w):
            c = '0'
            if i==0:
                c = str(1-j%2)
            elif i==1:
                if j==0 and (ans[i-1][j]=='0' and ans[i-1][j+1]=='0'):
                    c = '1'
                if j==w-1 and (ans[i-1][j]=='0' and ans[i-1][j-1]=='0'):
                    c = '1'
            elif i!=h-1:
                if (j==0 or j==w-1) and ans[i-1][j]=='0':
                    c = '1'
            else:
                if j==0:
                    if ans[i-1][j]=='0':
                        c = '1'
                elif j==1:
                    if ans[i-1][j-1]=='0' and line[-1]=='0':
                        c = '1'
                elif j==w-2:
                    if ans[i-1][j+1]=='0' and line[-1]=='0':
                        c = '1'
                elif j==w-1:
                    if ans[i-1][j]=='0' and line[-1]=='0':
                        c = '1'
                else:
                    if line[-1]=='0':
                        c = '1'
            line += c
        ans.append(line)
    for i in range(h):
        print(ans[i])
    print()
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
