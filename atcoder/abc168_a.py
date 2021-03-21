# https://atcoder.jp/contests/abc168/tasks/abc168_a

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = input()
if N[-1] == '3':
    print('bon')
elif N[-1] in ['0','1','6','8']:
    print('pon')
else:
    print('hon')


# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
