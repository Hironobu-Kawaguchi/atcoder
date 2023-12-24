# https://atcoder.jp/contests/abc328/tasks/abc328_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, X = map(int, input().split())
S = list(map(int, input().split()))

ans = 0
for i in range(N):
    if S[i] <= X:
        ans += S[i]
print(ans)
