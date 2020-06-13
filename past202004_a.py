# https://atcoder.jp/contests/past202004-open/tasks/past202004_a
# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

S, T = input().split()

def str2int(s):
    if s[0] == 'B':
        return 1-int(s[1])
    else:
        return int(s[0])

ans = abs(str2int(T) - str2int(S))
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
