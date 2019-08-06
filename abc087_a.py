# https://atcoder.jp/contests/abc087/tasks/abc087_a

X = int(input())
A = int(input())
B = int(input())

ans = X - A
ans = ans - (ans // B) * B

print(ans)
