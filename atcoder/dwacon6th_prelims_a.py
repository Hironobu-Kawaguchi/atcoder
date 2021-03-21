# https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_a

N = int(input())
s, t = [], []
for i in range(N):
    _s, _t = input().split()
    s.append(_s)
    t.append(int(_t))
X = input()

ans = 0
flg = False
for i in range(N):
    if flg:
        ans += t[i]
    if s[i] == X:
        flg = True
print(ans)
