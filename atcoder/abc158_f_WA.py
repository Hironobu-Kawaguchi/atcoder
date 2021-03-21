# https://atcoder.jp/contests/abc158/tasks/abc158_f

import bisect
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
MOD = 998244353

N = int(input())
robot = []
xs = []
for i in range(N):
    X, D = map(int, input().split())
    robot.append((X,X+D-1))
    xs.append(X)
xs.sort()
robot.sort()
ans = 1
for i in range(N):
    tmp = bisect.bisect_right(xs, robot[i][1]) - bisect.bisect_left(xs, robot[i][0])
    ans += pow(2, N-i-tmp, MOD) 

ans %= MOD
print(ans)
