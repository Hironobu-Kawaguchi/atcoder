# https://atcoder.jp/contests/abc018/tasks/abc018_1

A = int(input())
B = int(input())
C = int(input())

l = [A, B, C]
l.sort(reverse=True)
d = dict(zip(l, [1,2,3]))

print(d[A])
print(d[B])
print(d[C])
