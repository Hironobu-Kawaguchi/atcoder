# https://atcoder.jp/contests/abc134/tasks/abc134_b

N, D = map(int, input().split())

ans = - (N // -(2 * D + 1))
print(ans)
