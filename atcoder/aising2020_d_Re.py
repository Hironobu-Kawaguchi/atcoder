# https://atcoder.jp/contests/aising2020/tasks/aising2020_d

# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# @njit(cache=True)


# def main():
#     # @lru_cache(None)
#     # def dfs():
#     #     return
#     A, B = map(int, input().split())
#     print(A*B)
#     return

# def f(x):
#     mod = x.count('1')
#     n = int(x, 2)
#     return format(n%mod, 'b')

def f(x):
    X = len(x)
    mod = x.count('1')
    mod2 = format(mod, 'b')
    M = len(mod2)
    for i in range(X-M+1):
        if x[i:i+M] >= mod2:
            nx = int(x[i:i+M],2) % mod
            nx2 = format(nx, 'b')
            if i+M==X:
                x = '0' * (i+M-len(nx2)) + nx2
            else:
                x = '0' * (i+M-len(nx2)) + nx2 + x[i+M:]
        elif i+M==X:
            break
        elif x[i:i+M+1] >= '0'+mod2:
            nx = int(x[i:i+M+1],2) % mod
            nx2 = format(nx, 'b')
            if i+M==X-1:
                x = '0' * (i+M+1-len(nx2)) + nx2
            else:
                x = '0' * (i+M+1-len(nx2)) + nx2 + x[i+M+1:]
        # print(x)
    for i in range(X):
        if x[i] == '1':
            x = x[i:]
            break
    else:
        x = '0'
    return x

def f(x):
    X = len(x)
    mod = x.count('1')
    mod2 = format(mod, 'b')
    M = len(mod2)
    for i in range(X-M+1):
        if x[i:i+M] >= mod2:
            nx = int(x[i:i+M],2) % mod
            nx2 = format(nx, 'b')
            if i+M==X:
                x = '0' * (i+M-len(nx2)) + nx2
            else:
                x = '0' * (i+M-len(nx2)) + nx2 + x[i+M:]
        elif i+M==X:
            break
        elif x[i:i+M+1] >= '0'+mod2:
            nx = int(x[i:i+M+1],2) % mod
            nx2 = format(nx, 'b')
            if i+M==X-1:
                x = '0' * (i+M+1-len(nx2)) + nx2
            else:
                x = '0' * (i+M+1-len(nx2)) + nx2 + x[i+M+1:]
        # print(x)
    for i in range(X):
        if x[i] == '1':
            x = x[i:]
            break
    else:
        x = '0'
    return x

N = int(input())
X = input()
# print(X)
for i in range(N):
    if i==0:
        x = str(1-int(X[i])) + X[i+1:]
    elif i==N-1:
        x = X[:i] + str(1-int(X[i]))
    else:
        x = X[:i] + str(1-int(X[i])) + X[i+1:]
    ans = 0
    while x!='0':
        x = f(x)
        ans += 1
    print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
