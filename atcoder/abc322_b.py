# https://atcoder.jp/contests/abc322/tasks/abc322_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
S = input()
T = input()

if S == T[:N]:
    prefix = True
else:
    prefix = False
if S == T[-N:]:
    suffix = True
else:
    suffix = False

if prefix and suffix:
    print(0)
elif prefix:
    print(1)
elif suffix:
    print(2)
else:
    print(3)
