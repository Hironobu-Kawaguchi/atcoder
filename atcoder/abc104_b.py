# B - AcCepted
# https://atcoder.jp/contests/abc104/tasks/abc104_b

S = input()
n = len(S)

ans = 'AC'

if S[0] != 'A':
    ans = 'WA'

cnt = 0
for i in range(1, n):
    if S[i] == 'C' and (i >= 2 and i <= n-2):
        cnt += 1
    elif S[i] >= 'a' and S[i] <= 'z':
        continue
    else:
        ans = 'WA'
if cnt != 1:
    ans = 'WA'

print(ans)
