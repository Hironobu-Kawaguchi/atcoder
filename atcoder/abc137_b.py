# https://atcoder.jp/contests/abc137/tasks/abc137_b

K, X = map(int, input().split())

ans = []
for i in range(max(-1000000, X-K+1), min(X+K, 1000001)):
    ans.append(i)
print(*ans)
