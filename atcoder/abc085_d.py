# https://atcoder.jp/contests/abc085/tasks/abc085_d

N, H = map(int, input().split())
a, b = [], []
for i in range(N):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)
maxa = max(a)
b.sort(reverse=True)
ans = 0
tmp = 0
for i in range(N):
    if b[i] <= maxa:
        break
    ans += 1
    tmp += b[i]
    if tmp >= H:
        break
if tmp < H:
    ans += -(-(H-tmp) // maxa)

print(ans)
