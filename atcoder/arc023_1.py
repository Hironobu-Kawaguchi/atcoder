# https://atcoder.jp/contests/arc023/tasks/arc023_1

def days(y, m, d):
    if m in [1, 2]:
        y -= 1
        m += 12
    return 365*y + y//4 - y//100 + y//400 + 306*(m+1)//10 + d - 429

y = int(input())
m = int(input())
d = int(input())
print(days(2014, 5, 17) - days(y, m, d))
