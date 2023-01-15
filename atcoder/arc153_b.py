# https://atcoder.jp/contests/arc153/tasks/arc153_b

import sys
def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
# print(A)

Q = int(input())
si, sj = 0, 0
for qi in range(Q):
    a, b = map(int, input().split())
    if si<a:
        si = a - si - 1
    else:
        si = a - si + H - 1
    if sj<b:
        sj = b - sj - 1
    else:
        sj = b - sj + W - 1
# print(si, sj)

B = [[None for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if Q%2==0:
            ni = (si + i) % H
            nj = (sj + j) % W
        else:
            ni = (si - i + H) % H
            nj = (sj - j + W) % W
        B[ni][nj] = A[i][j]

for i in range(H):
    print(''.join(B[i]))



# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
