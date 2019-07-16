# C - Five Transportations
# https://atcoder.jp/contests/abc123/tasks/abc123_c

N = int(input())
l = [int(input()) for _ in range(5)]

bn = -(-N//min(l))
print(4 + bn)
print()