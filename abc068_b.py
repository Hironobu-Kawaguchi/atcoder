# https://atcoder.jp/contests/abc068/tasks/abc068_b

N = int(input())

i = 1
while 2**i <= N:
    i += 1
ans = 2 ** (i-1)
print(ans)
