# https://atcoder.jp/contests/abc012/tasks/abc012_2

N = int(input())
h = N // (60*60)
m = (N // 60) % 60
s = N % 60
print("{:02}:{:02}:{:02}".format(h, m, s))
