# https://atcoder.jp/contests/abc164/tasks/abc164_a

S, W = map(int, input().split())
if S <= W:
    print('unsafe')
else:
    print('safe')
