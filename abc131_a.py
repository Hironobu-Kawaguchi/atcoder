# https://atcoder.jp/contests/abc131/tasks/abc131_a

S = input()

ans = "Good"

for i in range(3):
    if S[i] == S[i+1]:
        ans = "Bad"

print(ans)
