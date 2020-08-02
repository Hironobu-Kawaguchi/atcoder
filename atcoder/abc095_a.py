# https://atcoder.jp/contests/abc095/tasks/abc095_a

S = input()

ans = 700
for i in range(3):
    if S[i] == 'o':
        ans += 100

print(ans)
