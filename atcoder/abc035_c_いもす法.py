# https://atcoder.jp/contests/abc035/tasks/abc035_c
# いもす法

N, Q = map(int, input().split())
imosu = [0] * (N+1)
for i in range(Q):
    l, r = map(int, input().split())
    imosu[l-1] += 1
    imosu[r] -= 1
  
now = 0
ans = ''
for j in range(N):
    now += imosu[j]
    if now % 2:
        ans += '1'
    else:
        ans += '0'
print(ans)
