# https://atcoder.jp/contests/aising2019/tasks/aising2019_a

n = int(input())
h = int(input())
w = int(input())
r = max(0, n-h+1)
c = max(0, n-w+1)
print(r*c)
