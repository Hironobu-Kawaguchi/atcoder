# https://atcoder.jp/contests/abc025/tasks/abc025_b

N, A, B = map(int, input().split())
ans = 0
for i in range(N):
    s, d = input().split()
    d = int(d)
    if s == "East":
        ans += min(max(d, A), B)
    else:
        ans -= min(max(d, A), B)
if ans == 0:
    print(ans)
elif ans > 0:
    print("East", ans)
else:
    print("West", -ans)
