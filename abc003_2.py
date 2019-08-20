# https://atcoder.jp/contests/abc003/tasks/abc003_2

S = input()
T = input()
at = ['a','t','c','o','d','e','r']

ans = "You can win"
for i in range(len(S)):
    if S[i] != T[i] and (S[i] != '@' or T[i] not in at) and (T[i] != '@' or S[i] not in at):
        ans = "You will lose"
        break
print(ans)
