# https://atcoder.jp/contests/arc069/tasks/arc069_b

from itertools import product
N = int(input())
s = input()
s += s[0]

def isOK(x, y):
    lst = [-1] * (N+2)
    lst[0] = x
    lst[1] = y
    for i in range(1, N+1):
        if (s[i] == 'o') ^ (lst[i]):    # 両隣は違う
            lst[i+1] = 1 - lst[i-1]
        else:                       # 両隣は同じ
            lst[i+1] = lst[i-1]
    if lst[0] == lst[-2] and lst[1] == lst[-1]:     # 1周回って同じ
        return lst[:-2]
    else:
        return []

for x, y in product([1,0], repeat=2):
    chk = isOK(x, y)
    if len(chk) > 0:
        break

if len(chk) == 0:
    ans = -1
else:
    ans = ''
    for x in chk:
        if x:
            ans += 'S'
        else:
            ans += 'W'
print(ans)
