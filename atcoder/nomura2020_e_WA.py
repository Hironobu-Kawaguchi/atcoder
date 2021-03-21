# https://atcoder.jp/contests/nomura2020/tasks/nomura2020_e
# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

T = list(map(int, input()))
# print(T)
ans = 0
for i in range(len(T)):
    ans += sum(T[::2])
    if 0 in T:
        T.remove(0)
    else:
        T.pop()
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
