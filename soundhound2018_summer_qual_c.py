# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_c

n, m, d = map(int, input().split())
if d == 0:
    ans = (m-1)/n
else:
    ans = (m-1)*2*(n-d)/(n*n)
print(ans)
