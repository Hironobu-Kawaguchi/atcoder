# https://atcoder.jp/contests/abc331/tasks/abc331_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d==D:
    m += 1
    d = 1
    if m==M+1:
        y += 1
        m = 1
else:
    d += 1

print(y, m, d)
