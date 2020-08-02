# https://atcoder.jp/contests/indeednow-quala/tasks/indeednow_2015_quala_2

a = sorted('indeednow')
n = int(input())
for _ in range(n):
    s = sorted(input())
    if s==a:
        print('YES')
        # print(s,a)
    else:
        print('NO')
