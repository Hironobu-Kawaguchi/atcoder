# https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_c
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())

def dfs(A, B, C):
    if A==a and B==b and C==c:
        return 1
    ans = 0
    if A!=a:
        ans += dfs(A+1, B, C)
    if A > B and B!=b:
        ans += dfs(A, B+1, C)
    if B > C and C!=c:
        ans += dfs(A, B, C+1)
    return ans

print(dfs(1,0,0))

# S = input()
# N = int(input())
# S, L, R = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
