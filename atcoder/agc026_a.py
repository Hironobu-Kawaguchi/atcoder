# A - Colorful Slimes 2
# https://atcoder.jp/contests/agc026/tasks/agc026_a

N = int(input())
a = list(map(int, input().split()))

ans = 0
tmp = 0
cnt = 1
for x in a:
    if x == tmp:
        cnt += 1
    else:
        tmp = x
        ans += cnt // 2
        cnt = 1
ans += cnt // 2
print(ans)
