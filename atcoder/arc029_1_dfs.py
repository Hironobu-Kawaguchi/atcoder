# A - 高橋君とお肉
# https://atcoder.jp/contests/arc029/tasks/arc029_1

def dfs(i, a, b):
    global ans
    if i == n:
        ans = min(ans, max(a, b))

    else:
        # a の肉焼き器に乗せるか、 b の肉焼き器に乗せるか
        dfs(i + 1, a + t[i], b)
        dfs(i + 1, a, b + t[i])


n = int(input())
t = [int(input()) for i in range(n)]

ans = float("inf")

dfs(0, 0, 0)
print(ans)