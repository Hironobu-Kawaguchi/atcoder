# https://atcoder.jp/contests/abc016/tasks/abc016_2

A, B, C = map(int, input().split())
if A + B == C and A - B == C:
    print('?')
elif A + B == C:
    print('+')
elif A - B == C:
    print('-')
else:
    print('!')
