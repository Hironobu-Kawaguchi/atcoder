# https://atcoder.jp/contests/abc326/tasks/abc326_a

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

X, Y = map(int, input().split())

if -3 <= Y - X <= 2:
    print('Yes')
else:
    print('No')
