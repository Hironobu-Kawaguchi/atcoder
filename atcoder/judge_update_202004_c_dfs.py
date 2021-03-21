# https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_c
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())
ans = 0

def dfs(A, B, C):
    global ans
    if A > a: return
    if B > b: return
    if C > c: return
    if A==a and B==b and C==c:
        ans += 1
        return
    dfs(A+1, B, C)
    if A > B:
        dfs(A, B+1, C)
    if B > C:
        dfs(A, B, C+1)

dfs(1,0,0)
print(ans)

# S = input()
# N = int(input())
# S, L, R = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
