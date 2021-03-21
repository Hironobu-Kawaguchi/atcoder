# https://atcoder.jp/contests/abc167/tasks/abc167_a

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

S = input()
T = input()

if S == T[:len(S)] and len(S)+1==len(T):
    print('Yes')
else:
    print('No')




# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
