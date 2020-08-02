# https://atcoder.jp/contests/arc097/tasks/arc097_b

n, m = map(int, input().split())
p = list(map(int, input().split()))
g = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
s = [0] * (n+1)
ans = 0
for i, j in enumerate(p, 1):
    q = [i]
    for k in q:
        if s[k]: continue
        s[k] = i
        q.extend(g[k])
    ans += (s[i] == s[j])
print(ans)
