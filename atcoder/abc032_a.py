# https://atcoder.jp/contests/abc032/tasks/abc032_a

a = int(input())
b = int(input())
n = int(input())

ans = n
while ans % a or ans % b:
    ans += 1

print(ans)
