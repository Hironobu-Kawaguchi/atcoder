# https://atcoder.jp/contests/abc013/tasks/abc013_3

N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ans = A*N
for x in range(N+1):
    y = ((N-x)*E - H - B*x) // (D+E) + 1
    y = max(min(y, N-x), 0)
    ans = min(ans, A*x+C*y)

print(ans)
