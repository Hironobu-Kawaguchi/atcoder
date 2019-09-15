# https://atcoder.jp/contests/abc141/tasks/abc141_b

S = input()

ans = "Yes"
for i in range(len(S)):
    if i % 2 and S[i] == 'R':
        ans = "No"
    elif i % 2 == 0 and S[i] == 'L':
        ans = "No"

print(ans)
