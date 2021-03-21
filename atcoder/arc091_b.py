# https://atcoder.jp/contests/arc091/tasks/arc091_b

n, k = map(int, input().split())
ans = 0
for b in range(k+1, n+1):
    ans += n//b * (b-k)
    ans += max((n%b)-k+1, 0)
if k == 0:
    # ans -= n
    ans = n*n
print(ans)
