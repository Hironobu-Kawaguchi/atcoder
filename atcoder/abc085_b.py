# https://atcoder.jp/contests/language-test-202001/tasks/abc085_b

N = int(input())
d = [int(input()) for _ in range(N)]
d.sort()

ans = 1
for i in range(N-1):
    if d[i] < d[i+1]:
        ans += 1
print(ans)
