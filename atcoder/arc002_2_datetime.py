# https://atcoder.jp/contests/arc002/tasks/arc002_2

from datetime import datetime, timedelta
s = input()
d = datetime.strptime(s, '%Y/%m/%d')

while d.year % (d.month * d.day):
    d += timedelta(1)
print(d.strftime('%Y/%m/%d'))
