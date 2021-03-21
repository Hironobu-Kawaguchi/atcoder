# https://atcoder.jp/contests/abc169/tasks/abc169_b

import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
A.sort()
ans = 1
for a in A:
    ans *= a
    if ans > 10**18:
        ans = -1
        break
    elif ans == 0:
        break
print(ans)

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
