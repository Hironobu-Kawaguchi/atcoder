# https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_b
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(a) + min(b)

for i in range(M):
    x, y, c = map(int, input().split())
    now = a[x-1] + b[y-1] - c
    ans = min(ans, now)
print(ans)
