# https://atcoder.jp/contests/arc011/tasks/arc011_1

m, n, N = map(int, input().split())
ans = N
used = N
while used >= m:
    tmp = used // m
    ans += tmp * n
    used -= tmp * (m-n)
print(ans)
