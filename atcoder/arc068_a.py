# https://atcoder.jp/contests/abc053/tasks/arc068_a

x = int(input())
q, mod = divmod(x, 11)
ans = q * 2 - (-mod // 6)
print(ans)
