# https://atcoder.jp/contests/abc147/tasks/abc147_b

S = input()
n = len(S)
ans = 0
for i in range(n//2):
    if S[i] != S[n-i-1]:
        ans += 1
print(ans)
