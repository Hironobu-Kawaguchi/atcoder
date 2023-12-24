# https://atcoder.jp/contests/abc330/tasks/abc330_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, L = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] >= L:
        ans += 1
print(ans)
