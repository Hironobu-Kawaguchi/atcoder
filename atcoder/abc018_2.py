# https://atcoder.jp/contests/abc018/tasks/abc018_2

S = input()
N = int(input())
l, r = [], []
for i in range(N):
    l_, r_ = map(int, input().split())
    l.append(l_)
    r.append(r_)

for i in range(N):
    ans = S[:l[i]-1] + S[l[i]-1:r[i]][::-1] + S[r[i]:]
    S = ans

print(ans)
