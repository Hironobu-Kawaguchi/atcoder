# https://atcoder.jp/contests/abc198/tasks/abc198_c


import math
R, X, Y = map(int, input().split())
dist = math.sqrt(X*X+Y*Y)
# print(dist)
ans = math.ceil(dist/R)
if ans==1 and dist!=R:
    ans = 2
print(ans)



# S = input()
# n = int(input())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
