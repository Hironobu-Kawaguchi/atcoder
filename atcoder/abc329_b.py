# https://atcoder.jp/contests/abc329/tasks/abc329_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
A.sort(reverse=True)
for i in range(N-1):
    if A[i] != A[i+1]:
        print(A[i+1])
        exit()
