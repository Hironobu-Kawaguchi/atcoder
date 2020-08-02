# https://atcoder.jp/contests/abc001/tasks/abc001_2

m = int(input())

if m < 100:
    ans = '00'
elif m <= 5000:
    if m < 1000:
        ans = '0' + str(m*10//1000)
    else:
        ans = str(m*10//1000)
elif m <= 30000:
    ans = str(m//1000 + 50)
elif m <= 70000:
    ans = str((m//1000 -30) //5 + 80)
else:
    ans = '89'

print(ans)
