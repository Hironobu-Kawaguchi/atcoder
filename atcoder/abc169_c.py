# https://atcoder.jp/contests/abc169/tasks/abc169_c

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

A, B = input().split()
b, c = B.split('.')
ans = int(A)*(int(b)*100+int(c))//100
print(ans)

# print(int(int(A)*float(B)))

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
