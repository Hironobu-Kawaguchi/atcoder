# https://atcoder.jp/contests/abc042/tasks/abc042_b

N, L = map(int, input().split())
S = [input() for _ in range(N)]
S.sort()
ans = ""
for i in range(N):
    ans += S[i]
print(ans)