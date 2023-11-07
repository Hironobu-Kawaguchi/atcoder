# https://atcoder.jp/contests/abc327/tasks/abc327_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

B = int(input())
for A in range(1, 18):
    if A**A==B:
        print(A)
        exit()
print(-1)
