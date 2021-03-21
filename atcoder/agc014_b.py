# https://atcoder.jp/contests/agc014/tasks/agc014_b

n, m = map(int, input().split())
d = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    d[a-1] ^= 1
    d[b-1] ^= 1
ans = 0
for j in range(n):
    ans |= d[j]
if ans:
    print("NO")
else:
    print("YES")
