# https://atcoder.jp/contests/abc084/tasks/abc084_d

Q = int(input())
l, r = [], []
for i in range(Q):
    _l, _r = map(int, input().split())
    l.append(_l)
    r.append(_r)
max_r = max(r)

is_sosu = [1] * (max_r + 1)
is_sosu[0] = is_sosu[1] = 0
for i in range(2, max_r+1):
    if is_sosu[i]:
        for j in range(i*i, max_r+1, i):
            is_sosu[j] = 0

sums = [0] * (max_r + 1)
for i in range(1, max_r+1):
    if is_sosu[i] and is_sosu[(i+1)//2]:
        sums[i] = sums[i-1] + 1
    else:
        sums[i] = sums[i-1]

for i in range(Q):
    print(sums[r[i]] - sums[l[i]-1])
