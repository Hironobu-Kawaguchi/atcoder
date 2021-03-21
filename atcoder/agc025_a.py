# https://atcoder.jp/contests/agc025/tasks/agc025_a

N = input()

ans = 0
for i in range(len(N)):
    ans += int(N[i])

if ans == 1:
    ans = 10

print(ans)
