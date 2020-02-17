# https://atcoder.jp/contests/abc155/tasks/abc155_d

import sys
input = sys.stdin.buffer.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def ok(x):
    res = 0
    for i in range(N):
        if A[i]<0:
            left, right = -1, N
            while left + 1 < right:
                c = (left + right) // 2
                if A[c]*A[i] < x: right = c
                else:             left  = c
            res += N - right
        else:
            left, right = -1, N
            while left + 1 < right:
                c = (left + right) // 2
                if A[c]*A[i] < x: left  = c
                else:             right = c
            res += right
        if A[i]*A[i] < x:
            res -= 1
    res //= 2
    return res < K

INF = 10**18+1
l, r = -INF, INF
while l+1<r:
    x = (l+r)//2
    if ok(x):
        l = x
    else:
        r = x
print(l)
