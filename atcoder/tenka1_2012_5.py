# https://atcoder.jp/contests/tenka1-2012-qualB/tasks/tenka1_2012_5

a, b, c = map(int, input().split())
for i in range(1,128):
    if i%3==a and i%5==b and i%7==c:
        print(i)
