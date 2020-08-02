# https://atcoder.jp/contests/nomura2020/tasks/nomura2020_b
# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

T = input()
ans = ''
for c in T:
    if c=='?':
        c = 'D'
    ans += c
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
