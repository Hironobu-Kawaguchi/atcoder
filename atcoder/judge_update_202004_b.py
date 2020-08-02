# https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_b
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N = int(input())
balls = []
for i in range(N):
    x, c = input().split()
    if c == 'R':
        y = 0
    else:
        y = 1
    x = int(x)
    balls.append([y,x])
balls.sort()
# print(balls)
for i in range(N):
    print(balls[i][1])


# S = input()
# S, L, R = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
