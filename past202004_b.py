# https://atcoder.jp/contests/past202004-open/tasks/past202004_b
# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from collections import Counter
S = input()
cnt = Counter(S)

ans = ''
tmp = 0
for k, v in cnt.items():
    if v > tmp:
        ans = k
        tmp = v
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
