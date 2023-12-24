# https://atcoder.jp/contests/abc324/tasks/abc324_e

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import sys
import bisect

N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

left = [-1] * N
for i in range(N):
    now = 0
    for j in range(len(S[i])):
        if S[i][j]==T[now]:
            now += 1
            if now==len(T):
                left[i] = now - 1
                break
    else:
        left[i] = now - 1
right = [-1] * N
for i in range(N):
    now = len(T) - 1
    for j in range(len(S[i])-1, -1, -1):
        if S[i][j]==T[now]:
            now -= 1
            if now==-1:
                right[i] = now + 1
                # print("check", file=sys.stderr)
                break
    else:
        right[i] = now + 1
# print(left)
# print(right)

right.sort()
ans = 0
for i in range(N):
    ans += bisect.bisect_right(right, left[i] + 1)

print(ans)
