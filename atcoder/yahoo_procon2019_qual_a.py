# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_a

n, k = map(int, input().split())
if n >= 2*k-1:
    print('YES')
else:
    print('NO')
