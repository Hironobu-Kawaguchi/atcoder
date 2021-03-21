# https://atcoder.jp/contests/abc064/tasks/abc064_d

N = int(input())
S = input()
l, r = 0, 0
lp, rp = 0, 0

for i in range(N):
    if S[i] == '(':
        l += 1
    else:
        r += 1
    lp = max(lp, r-l)
rp = lp + l - r

ans = '(' * lp + S + ')' * rp
print(ans)
