# https://atcoder.jp/contests/abc017/tasks/abc017_1
ans = 0
for i in range(3):
    s, e = map(int, input().split())
    ans += s * e // 10
print(ans)
