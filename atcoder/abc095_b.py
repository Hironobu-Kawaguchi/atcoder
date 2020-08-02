# https://atcoder.jp/contests/abc095/tasks/abc095_b

N ,X = map(int, input().split())
m = [int(input()) for _ in range(N)]

ans = N + (X - sum(m)) // min(m)

print(ans)
