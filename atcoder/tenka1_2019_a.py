# A - On the Way
# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_a

A, B, C = map(int, input().split())

if ( A > C and C > B ) or ( B > C and C > A ):
    print('Yes')
else:
    print('No')
    