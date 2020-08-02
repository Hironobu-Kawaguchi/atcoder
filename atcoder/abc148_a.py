# https://atcoder.jp/contests/abc148/tasks/abc148_a

A = int(input())
B = int(input())
for i in range(3):
    if A == i+1 or B == i+1:
        continue
    else:
        print(i+1)
