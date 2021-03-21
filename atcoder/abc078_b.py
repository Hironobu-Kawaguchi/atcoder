# https://atcoder.jp/contests/abc078/tasks/abc078_b

X, Y, Z = map(int, input().split())
ans = (X - Z) // (Y + Z)
print(ans)