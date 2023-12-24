# https://atcoder.jp/contests/abc324/tasks/abc324_b

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())

while N%2==0:
    N //= 2

while N%3==0:
    N //= 3

if N==1:
    print("Yes")
else:
    print("No")
