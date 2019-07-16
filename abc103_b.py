# https://atcoder.jp/contests/abc103/tasks/abc103_b

S = input()
T = input()
n = len(S)

ans = 'No'
for i in range(n):
    if S[-i:] + S[:-i] == T:
        ans = 'Yes'
print(ans)
