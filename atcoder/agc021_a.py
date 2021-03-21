# https://atcoder.jp/contests/agc021/tasks/agc021_a

S = input()
keta = len(S)

chk = True
for i in range(keta-1):
    if S[i+1] != '9':
        chk = False
        break

if chk:
    ans = 9 * (keta-1) + int(S[0])
else:
    ans = 9 * (keta-1) + int(S[0]) - 1

print(ans)
