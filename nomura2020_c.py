# https://atcoder.jp/contests/nomura2020/tasks/nomura2020_c
import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
tmp = sum(A)
root = 0
ans = 0
for i in range(N+1):
    if i==0:
        mx = 1
    else:
        mx = root*2
    if A[i] > mx:
        ans = -1
        break
    root = min(tmp, mx) - A[i]
    tmp -= A[i]
    ans += root + A[i]

print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
