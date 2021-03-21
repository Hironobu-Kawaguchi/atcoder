# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_a

rl = []
N = int(input())
for i in range(N):
    x, l = map(int, input().split())
    rl.append((x+l, x-l))
rl.sort()

ans = 0
tmp = rl[0][0]
for i in range(N):
    if i and rl[i][1] < tmp:
        continue
    tmp = rl[i][0]
    ans += 1
print(ans)
