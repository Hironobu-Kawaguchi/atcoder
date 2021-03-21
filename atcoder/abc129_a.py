# 
# https://atcoder.jp/contests/abc129/tasks/abc129_a

P, Q, R = map(int, input().split())

ans = (P + Q + R) - max(max(P, Q), R)
print(ans)
