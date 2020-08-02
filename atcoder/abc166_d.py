# https://atcoder.jp/contests/abc166/tasks/abc166_d
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def f(y, b):
    return y**4 + 5*(y**3)*b + 10*(y**2)*(b**2) + 10*y*(b**3) + 5*(b**4)

X = int(input())
for y in range(1, int(X**0.5)+1):
    if X%y==0:
        tmp = X//y
        right = int(tmp**(1/4))+1
        left = -right
        while left < right:
            b = (right + left)//2
            fyb = f(y, b)
            if  fyb == tmp:
                break
            elif fyb > tmp:
                right = b
            else:
                left = b + 1
        if fyb == tmp:
            break
print(y+b, b)

# S = input()
# N, M = map(int, input().split())
# H = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]