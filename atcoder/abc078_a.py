# https://atcoder.jp/contests/abc078/tasks/abc078_a

X, Y = input().split()

if X < Y:
    print('<')
elif X > Y:
    print('>')
else:
    print('=')
