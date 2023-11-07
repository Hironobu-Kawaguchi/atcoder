# https://atcoder.jp/contests/abc326/tasks/abc326_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())

for i in range(N, 1000):
    c, b = i % 10, i // 10
    b, a = b % 10, b // 10
    if a * b == c:
        print(i)
        exit()
