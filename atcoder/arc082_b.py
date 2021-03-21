# https://atcoder.jp/contests/abc072/tasks/arc082_b

N = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    if p[i] == i+1:
        a, b = p[i], p[i+1]
        p[i], p[i+1] = b, a
        ans += 1
if p[N-1] == N:
    ans += 1

print(ans)
