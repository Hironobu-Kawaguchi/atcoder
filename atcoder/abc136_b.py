# https://atcoder.jp/contests/abc136/tasks/abc136_b

N = int(input())
keta = len(str(N))

ans = 0
for i in range(keta-1):
    if i % 2 == 0:
        ans += 10 ** i * 9
if keta % 2:
    ans += N - 10 ** (keta-1) + 1
print(ans)
