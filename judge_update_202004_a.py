# https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_a
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

S, L, R = map(int, input().split())
if S < L:
    ans = L
elif S <= R:
    ans = S
else:
    ans = R
print(ans)


# S = input()
# n = int(input())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
