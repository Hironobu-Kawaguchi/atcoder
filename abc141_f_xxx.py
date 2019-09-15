# https://atcoder.jp/contests/abc141/tasks/abc141_f

N = int(input())
A = list(map(int, input().split()))

ans = 0

def dfs(i, red, blue, r, b):
    if i >= N:
        return
    if red == 0:
        dfs(i+1, A[i], blue, r+1, b)
        dfs(i+1, red, blue ^ A[i], r, b+1)
    elif blue == 0:
        dfs(i+1, red ^ A[i], blue, r+1, b)
        dfs(i+1, red, A[i], r, b+1)
    else:
        dfs(i+1, red ^ A[i], blue, r+1, b)
        dfs(i+1, red, blue ^ A[i], r, b+1)
    if i == N-1:
        global ans
        ans = max(ans, red + blue)

dfs(0,0,0,0,0)
# ans = 6 + 3^5
print(ans)
