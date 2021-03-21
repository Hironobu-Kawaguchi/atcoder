# https://atcoder.jp/contests/abc014/tasks/abc014_3
# いもす法

n = int(input())
cum = [0] * 1000002
for i in range(n):
    a, b = map(int, input().split())
    cum[a] += 1
    cum[b+1] -= 1
ans = 0
tmp = 0
for c in cum:
    if c != 0:
        tmp += c
        ans = max(ans, tmp)
print(ans)
