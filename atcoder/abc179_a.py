# https://atcoder.jp/contests/abc179/tasks/abc179_a

S = input()
if S[-1]=='s':
    ans = S + 'es'
else:
    ans = S + 's'
print(ans)
